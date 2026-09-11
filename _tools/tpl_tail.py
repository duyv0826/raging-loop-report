# -*- coding: utf-8 -*-
"""收尾两处清单尾件差异：ch01 补等级说明行，ch06 表头统一为「类型（阶梯）」。"""

TIER = '> 各条目的来源等级（S1–S7）依《00-conflict-rulings.md》第 1 节的阶梯判定；终稿参考文献统一标注。'

SPECS = {
    'chapters/ch01.md': [
        {'ln': (154, 154), 'has': 'Reference.org', 'new': '\n' + TIER, 'insert_after': True},
    ],
    'chapters/ch06.md': [
        {'ln': (65, 65), 'has': '本报告阶梯', 'new': '| # | 来源 | 类型（阶梯） | URL |'},
    ],
}

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '_tools')
    from patchlib import apply
    ok = True
    for fname, patches in SPECS.items():
        if not apply(fname, patches):
            ok = False
    sys.exit(0 if ok else 1)
