# -*- coding: utf-8 -*-
"""按各章真实标题重排前置框架的「目录」，避免手工维护漂移。
规则：收录 ## 与带编号的 ### （如 1.2.1／4.4.1）；
      章末三件套（本章引用来源清单／存疑与事实冲突说明）不单列，改为章首统一说明。
"""
import io
import re
import glob



def collect(path):
    rows = []
    for l in io.open(path, encoding='utf-8').read().split('\n'):
        title = l.lstrip('#').strip()
        if l.startswith('## ') and re.match(r'^\d+\.\d+(\s|$)', title):
            rows.append('  - ' + title)
        elif l.startswith('### ') and re.match(r'^\d+\.\d+\.\d+(\s|$)', title):
            rows.append('    - ' + title)
    return rows


def main():
    paths = sorted(glob.glob('chapters/ch*.md'))
    assert len(paths) == 6, paths
    out = ['- 研究引言', '- 目录']
    for p in paths:
        lines = io.open(p, encoding='utf-8').read().split('\n')
        h1 = [l for l in lines if l.startswith('# ')]
        assert h1, p
        out.append('- ' + h1[0][2:].strip())
        out += collect(p)
    out.append('- 研究结论')
    out.append('- 参考文献')
    toc = '\n'.join(out)

    f = '_report_frontback.md'
    lines = io.open(f, encoding='utf-8').read().split('\n')
    i = lines.index('## 目录')
    j = next(k for k in range(i + 1, len(lines)) if lines[k] == '---')
    old = lines[i + 1:j]
    assert any(l.startswith('- 引言') for l in old), 'TOC region not found'
    note = ('> 各章末统一附「本章引用来源清单」（含 S1–S7 来源等级）与「存疑与事实冲突说明」两节，'
            '因体例一致、不另列于目录。')
    lines[i + 1:j] = ['', note, ''] + out + ['']
    io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
    print('TOC replaced: %d lines -> %d lines' % (len(old), len(out) + 2))


if __name__ == '__main__':
    main()
