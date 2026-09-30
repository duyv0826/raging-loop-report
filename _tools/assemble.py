# -*- coding: utf-8 -*-
"""把前置框架与六章正文装配为单文件终稿。

装配顺序（依前置框架自身的说明）：
标题 → 跨章口径 → 研究引言 → 目录 → 第1–6章 → 研究结论 → 参考文献 → 后置附录

后置附录（附：玩家社区声音／附录 A／附录 B）与正文同源，一律取自
_report_frontback.md 的同名小节：附录只写在终稿里等于没写——重跑本脚本
即被覆盖。故所有交付文本内容一律改源文件，不改终稿。

丢弃的前置件内部脚手架：框架文档标题、「本文档为 Phase 5 终稿整合用…」说明、
文末「本框架文档为前置／后置件…」斜体注。装配后跑自检，任何一项不过即不写盘。
"""
import io
import os
import re
import glob
import sys

OUT = '终稿_人狼村之谜研究报告.md'
FB = '_report_frontback.md'
NL = '\n'
TITLE = '# 《人狼村之谜》深度研究报告'
BAN = ('00-conflict-rulings', 'Phase 5', '工作副本', '前置／后置件', '事实核查报告')
POST = ('附：玩家社区声音（2026-09，一手自述）',
        '附录 A　事实核验补充记录（2026-09-30 复核）',
        '附录 B　30 秒实机自证操作（暴露模式）')


def section(text, heading):
    """取 '## heading' 到下一个 '---' 分隔线之间的内容（含标题行）。"""
    lines = text.split(NL)
    i = lines.index('## ' + heading)
    j = next(k for k in range(i + 1, len(lines)) if lines[k] == '---')
    return lines[i:j]


def tail_section(text, heading):
    """同 section，但去掉小节末尾紧邻分隔线的空行，避免装配出连续空行。"""
    lines = section(text, heading)
    while lines and lines[-1] == '':
        lines.pop()
    return lines


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
    parts += tail_section(fb, '研究结论') + ['---', '']
    parts += tail_section(fb, '参考文献')
    for h in POST:
        parts += ['', '---', ''] + tail_section(fb, h)
    doc = NL.join(parts).rstrip(NL) + NL

    # ---- 自检 ----
    fails = []
    h1 = [l for l in doc.split(NL) if l.startswith('# ')]
    want = [TITLE] + ['# 第%d章' % n for n in range(1, 7)]
    if [h[:len(w)] for h, w in zip(h1, want)] != want or len(h1) != 6 + 1:
        fails.append('章标题序列不符: %s' % h1)
    order = [doc.index(x) for x in ['## 研究引言', '## 目录', '# 第1章', '# 第6章',
                                    '## 研究结论', '## 参考文献'] + ['## ' + h for h in POST]]
    if order != sorted(order):
        fails.append('节序错乱: %s' % order)
    for h in POST:
        if doc.count('## ' + h) != 1:
            fails.append('后置附录缺失或重复: %s（%d 次）' % (h, doc.count('## ' + h)))
    if doc.rstrip(NL).split(NL)[-1] != '> 说明：若无实机条件，可用 2 张对照截图（普通模式 vs 暴露模式同一段落）替代演示；截图中红色文本框可见即可。':
        fails.append('终稿未以附录 B 收尾，末行为: %s' % doc.rstrip(NL).split(NL)[-1][:40])
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
    refs_end = next(k for k in range(tail.index('## 参考文献'), len(tail))
                    if k > tail.index('## 参考文献') and tail[k].startswith('## '))
    refs = [l for l in tail[tail.index('## 参考文献'):refs_end] if re.match(r'^\d+\. ', l)]
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
    # 自检已过，落盘仍可能中断（磁盘满 / 编码炸 / 后续改坏的源文件触发新 assert），
    # 故先备份再写：宁可留一个待人工清理的 _backup_prev_*，也不留半截交付稿。
    backup = None
    try:
        if os.path.isfile(OUT):
            backup = '_tools/_backup_prev_' + OUT
            with open(OUT, 'rb') as src, open(backup, 'wb') as dst:
                dst.write(src.read())
        tmp = OUT + '.tmp'
        with io.open(tmp, 'w', encoding='utf-8', newline=NL) as f:
            f.write(doc)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, OUT)
        if backup and os.path.isfile(backup):
            os.remove(backup)
    except Exception as exc:
        print('WRITE ABORTED, nothing lost:', repr(exc))
        if backup and os.path.isfile(OUT):
            with open(backup, 'rb') as src, open(OUT, 'wb') as dst:
                dst.write(src.read())
        for stray in (OUT + '.tmp',):
            if os.path.isfile(stray):
                os.remove(stray)
        sys.exit(2)
    print('written %s: %d lines, %d chars' % (OUT, doc.count(NL), len(doc)))


if __name__ == '__main__':
    main()
