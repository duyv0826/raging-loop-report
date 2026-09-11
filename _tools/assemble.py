# -*- coding: utf-8 -*-
"""把前置框架与六章正文装配为单文件终稿。

装配顺序（依前置框架自身的说明）：
标题 → 跨章口径 → 研究引言 → 目录 → 第1–6章 → 研究结论 → 参考文献

丢弃的前置件内部脚手架：框架文档标题、「本文档为 Phase 5 终稿整合用…」说明、
文末「本框架文档为前置／后置件…」斜体注。装配后跑自检，任何一项不过即不写盘。
"""
import io
import re
import glob
import sys

OUT = '终稿_人狼村之谜研究报告.md'
FB = '_report_frontback.md'
NL = '\n'
TITLE = '# 《人狼村之谜》深度研究报告'
BAN = ('00-conflict-rulings', 'Phase 5', '工作副本', '前置／后置件')


def section(text, heading):
    """取 '## heading' 到下一个 '---' 分隔线之间的内容（含标题行）。"""
    lines = text.split(NL)
    i = lines.index('## ' + heading)
    j = next(k for k in range(i + 1, len(lines)) if lines[k] == '---')
    return lines[i:j]


def main():
    fb = io.open(FB, encoding='utf-8').read()
    kj = [l for l in fb.split(NL) if l.startswith('> 跨章口径')]
    assert len(kj) == 1, kj

    parts = [TITLE, '', kj[0], '', '---', '']
    parts += section(fb, '研究引言') + ['---', '']
    parts += section(fb, '目录') + ['---', '']
    for p in sorted(glob.glob('chapters/ch*.md')):
        body = io.open(p, encoding='utf-8').read().rstrip(NL)
        parts += body.split(NL) + ['', '---', '']
    parts += section(fb, '研究结论') + ['---', '']
    parts += section(fb, '参考文献')
    doc = NL.join(parts).rstrip(NL) + NL

    # ---- 自检 ----
    fails = []
    h1 = [l for l in doc.split(NL) if l.startswith('# ')]
    want = [TITLE] + ['# 第%d章' % n for n in range(1, 7)]
    if [h[:len(w)] for h, w in zip(h1, want)] != want or len(h1) != 6 + 1:
        fails.append('章标题序列不符: %s' % h1)
    order = [doc.index(x) for x in ['## 研究引言', '## 目录', '# 第1章', '# 第6章',
                                    '## 研究结论', '## 参考文献']]
    if order != sorted(order):
        fails.append('节序错乱: %s' % order)
    for b in BAN:
        if b in doc:
            fails.append('残留内部脚手架: %s' % b)
    m = re.search(NL + '{3,}', doc)
    if m:
        fails.append('第 %d 行附近存在连续空行' % (doc[:m.start()].count(NL) + 1))
    if '\r' in doc:
        fails.append('存在 CR 字符（源文件应为 LF）')
    if re.search(r'\bE\d\b', doc):
        fails.append('残留内部证据代号 E<n>')
    tail = doc.split(NL)
    refs = [l for l in tail[tail.index('## 参考文献'):] if re.match(r'^\d+\. ', l)]
    if len(refs) != 49:
        fails.append('参考文献条数 %d != 49' % len(refs))
    src = NL.join(io.open(p, encoding='utf-8').read()
                  for p in [FB] + sorted(glob.glob('chapters/ch*.md')))
    for u in set(re.findall(r'https?://[^\s)）】>」]+', doc)):
        if u not in src:
            fails.append('终稿出现来源文件中不存在的 URL: %s' % u[:70])
    if doc.count('**') % 2 or doc.count('`') % 2:
        fails.append('加粗或反引号不成对')
    for s in ('## 本章引用来源清单', '## 存疑与事实冲突说明'):
        if doc.count(s) != 6:
            fails.append('%s 出现 %d 次（应为 6）' % (s, doc.count(s)))

    if fails:
        print('ABORT, nothing written:')
        for f in fails:
            print('  -', f)
        sys.exit(1)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(doc)
    print('written %s: %d lines, %d chars' % (OUT, doc.count(NL), len(doc)))


if __name__ == '__main__':
    main()
