# -*- coding: utf-8 -*-
"""终稿一致性核验（只读，不写入）。
1) 参考文献编号表 ⇄ 六章正文实际引用：双向集合相等
2) 每条编号项均带 S 等级、URL 与被引章标注；编号连续
3) 备查段的 URL 确实零引用（不与正文引用集相交）
4) 目录 ⇄ 各章真实标题：无缺漏、无多余
5) 前置框架节序：研究引言 / 目录 / 研究结论 / 参考文献
6) 全文无未闭合的 ** 加粗与反引号
"""
import io
import re
import glob
import sys

sys.path.insert(0, '_tools')
from gen_refs import norm, extract_urls, chapter_data, global_list  # noqa: E402

FB = '_report_frontback.md'
out = []
fails = []


def check(cond, msg):
    (out if cond else fails).append(('OK  ' if cond else 'FAIL') + ' ' + msg)


fb = io.open(FB, encoding='utf-8').read()
meta, cited = chapter_data()
gitems = global_list(fb)

# 1 + 2
gurls = {}
for n, s in gitems:
    us = [norm(u) for u in extract_urls(s)]
    check(len(us) == 1, '#%d 恰含一个 URL (%s)' % (n, s[:40]))
    gurls[us[0]] = s
check([n for n, _ in gitems] == list(range(1, len(gitems) + 1)), '编号连续 1..%d' % len(gitems))
check(set(gurls) == set(cited), '参考文献编号表与正文引用集合相等（表=%d 正文=%d）' % (len(gurls), len(cited)))
for k, s in sorted(gurls.items()):
    check(re.search(r'S\d', s) is not None, '#等级标注 %s' % k[:46])
    check('〔第' in s and '章引用〕' in s, '#被引章标注 %s' % k[:46])

# 3
i = fb.index('未采信／备查来源')
j = fb.index('\n---\n', i)
spare = [norm(u) for u in extract_urls(fb[i:j])]
check(len(spare) == 7, '备查段 7 条（实际 %d）' % len(spare))
check(not (set(spare) & set(cited)), '备查段 URL 均未被正文引用')

# 4
lines = fb.split('\n')
a = lines.index('## 目录')
b = next(k for k in range(a + 1, len(lines)) if lines[k] == '---')
toc = [l.strip()[2:] for l in lines[a:b] if re.match(r'^\s*- ', l)]
real = ['研究引言', '目录']
for p in sorted(glob.glob('chapters/ch*.md')):
    for l in io.open(p, encoding='utf-8').read().split('\n'):
        t = l.lstrip('#').strip()
        if l.startswith('# ') or (l.startswith('## ') and re.match(r'^\d+\.\d+(\s|$)', t)) \
           or (l.startswith('### ') and re.match(r'^\d+\.\d+\.\d+', t)):
            real.append(t)
real += ['研究结论', '参考文献']
check(toc == real, '目录与真实标题逐条一致（目录=%d 实际=%d）' % (len(toc), len(real)))
if toc != real:
    out.append('     缺: %s' % [t for t in real if t not in toc])
    out.append('     多: %s' % [t for t in toc if t not in real])

# 5
order = [l for l in lines if re.match(r'^## (研究引言|目录|研究结论|参考文献)$', l)]
check(order == ['## 研究引言', '## 目录', '## 研究结论', '## 参考文献'], '前置框架节序 %s' % order)

# 5b 来源阶梯在前置框架中只出现一次（builder 重复运行曾造成整段重复插入）
check(fb.count('**来源优先级阶梯（S1–S7）。**') == 1,
      '来源阶梯仅插入一次（实际 %d）' % fb.count('**来源优先级阶梯（S1–S7）。**'))
check(fb.count('| **S1** |') == 1, '阶梯表 S1 行唯一')
check(fb.count('阶梯三条例外规则') == 1, '例外规则段唯一')

# 6
for p in [FB] + sorted(glob.glob('chapters/ch*.md')):
    t = io.open(p, encoding='utf-8').read()
    check(t.count('**') % 2 == 0, '%s 加粗标记成对 (%d)' % (p, t.count('**')))
    check(t.count('`') % 2 == 0, '%s 反引号成对 (%d)' % (p, t.count('`')))
    check('\r' not in t, '%s 无 CR' % p)

io.open('_tools/_verify.txt', 'w', encoding='utf-8', newline='\n').write(
    '\n'.join(fails) + '\n\n--- PASS (%d) ---\n' % len(out) + '\n'.join(out) + '\n')
print('FAIL=%d PASS=%d' % (len(fails), len(out)))
