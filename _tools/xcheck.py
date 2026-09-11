# -*- coding: utf-8 -*-
"""章末清单与正文内联引用的双向核对。
归一化：URL 解码、去 www.、去尾斜杠、萌娘百科多域名/多编码写法归一。
"""
import io
import re
import glob
import urllib.parse

MOE = re.compile(r'^(https?://)(?:www\.|m\.)?(zh\.moegirl\.(?:org\.cn|tw|com)|moegirl\.org\.cn)(/.*)?$')
URL = re.compile(r'https?://[^\s)\]）】>」]+')


def norm(u):
    u = u.rstrip('.,;、。）)')
    u = urllib.parse.unquote(u)
    m = MOE.match(u)
    if m:
        path = (m.group(3) or '').rstrip('/')
        return 'MOEGIRL' + path
    u = u.replace('https://', 'http://')
    u = re.sub(r'^http://(www\.)?', 'http://', u)
    return u.rstrip('/')


def body_and_list(text):
    i = text.index('## 本章引用来源清单')
    j = text.index('## 存疑与事实冲突说明')
    return text[:i] + text[j:], text[i:j]


out = []
for f in sorted(glob.glob('chapters/ch*.md')):
    text = io.open(f, encoding='utf-8').read()
    body, lst = body_and_list(text)
    in_text = {norm(u) for u in URL.findall(body)}
    listed = {norm(u) for u in URL.findall(lst)}
    missing = sorted(in_text - listed)
    unused = sorted(listed - in_text)
    out.append('===== %s  in-text=%d listed=%d' % (f, len(in_text), len(listed)))
    out.append('  未在清单中的正文链接 (%d):' % len(missing))
    out += ['     ' + u for u in missing]
    out.append('  清单未被正文引用 (%d):' % len(unused))
    out += ['     ' + u for u in unused]

io.open('_tools/_x.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('written')
