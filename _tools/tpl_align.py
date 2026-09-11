# -*- coding: utf-8 -*-
"""清单与正文引用对齐：
1) ch03 正文内 雾雨小镇 链接统一为清单里的规范写法（去掉 ordertype=1 排序参数）；
2) ch02 清单删除正文未实际引用的两行（快懂百科、Fandom 主条目），并顺序重编号。
"""
import io
import re

# --- 1) ch03 URL 规范化 ---
f3 = 'chapters/ch03.md'
t3 = io.open(f3, encoding='utf-8').read()
n3 = t3
for pat in ('?mod=viewthread&tid=11182&ordertype=1', '?mod=viewthread&ordertype=1&tid=11182'):
    n3 = n3.replace(pat, '?mod=viewthread&tid=11182')
cnt = t3.count('ordertype=1')
if n3 != t3:
    io.open(f3, 'w', encoding='utf-8', newline='\n').write(n3)
print('ch03 ordertype occurrences fixed:', cnt, '-> remaining:', n3.count('ordertype=1'))

# --- 2) ch02 清单瘦身 ---
f2 = 'chapters/ch02.md'
lines = io.open(f2, encoding='utf-8').read().split('\n')
DROP = ('baike.com/wikiid/3632591420506430650', 'ragingloop.fandom.com/wiki/Raging_Loop')
rows = [(i, l) for i, l in enumerate(lines) if re.match(r'^\| \d+ \|', l) and i > 135]
assert len(rows) == 17, 'unexpected ch02 row count: %d' % len(rows)
keep, dropped = [], []
for i, l in rows:
    (dropped if any(d in l for d in DROP) else keep).append((i, l))
assert len(dropped) == 2, 'expected to drop exactly 2 rows, got %d' % len(dropped)
for n, (i, l) in enumerate(keep, 1):
    lines[i] = re.sub(r'^\| \d+ \|', '| %d |' % n, l)
for i, _ in dropped:
    lines[i] = None
lines = [l for l in lines if l is not None]
io.open(f2, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('ch02 rows: 17 ->', len(keep))
