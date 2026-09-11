# -*- coding: utf-8 -*-
"""终稿参考文献重建 · 第一阶段：只统计不写入。
产出 _tools/_refs.txt：
  A) 全局清单里有、但六章正文从未引用的条目（应删或补引）
  B) 正文引用了、但全局清单缺失的条目（应补）
  C) 每条被引 URL 的元数据（来源名／类型等级／被引章）与多写法归并情况
"""
import io
import re
import glob
import urllib.parse
from collections import Counter

FB = '_report_frontback.md'
MOE = re.compile(r'^(?:https?://)(?:[a-z0-9-]+\.)*moegirl\.(?:org\.cn|tw|com)(/zh-(?:hant|hans|cn|tw))?(/.*)?$')
URL = re.compile(r'https?://[^\s)\]）】>」]+')


def extract_urls(text):
    """提取 URL；若因成对括号被截断，补回缺失的右括号。"""
    res = []
    for u in URL.findall(text):
        while u.count('(') > u.count(')'):
            u += ')'
        res.append(u)
    return res


def norm(u):
    u = u.rstrip('.,;、）)')
    u = urllib.parse.unquote(u)
    m = MOE.match(u)
    if m:
        return 'MOEGIRL' + (m.group(2) or '').rstrip('/')
    u = re.sub(r'^https?://(www\.)?', 'http://', u)
    return u.rstrip('/')


def global_list(text):
    """返回 [(idx, raw_entry)]，取 ## 参考文献 下的有序列表项。"""
    i = text.index('## 参考文献')
    j = text.index('\n---\n', i)
    block = text[i:j]
    k = block.find('未采信／备查来源')
    if k >= 0:
        block = block[:k]
    items = re.findall(r'^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|ZEND)',
                       block + 'ZEND', re.M | re.S)
    return [(int(n), ' '.join(s.split())) for n, s in items]


def chapter_data():
    """{norm_url: {'names':set,'types':set,'raws':set,'ch':set}} + 每章正文引用集合"""
    meta = {}
    cited = {}
    for p in sorted(glob.glob('chapters/ch*.md')):
        ch = re.search(r'ch0(\d)', p).group(1)
        text = io.open(p, encoding='utf-8').read()
        i = text.index('## 本章引用来源清单')
        j = text.index('## 存疑与事实冲突说明')
        body = text[:i] + text[j:]
        lst = text[i:j]
        for u in extract_urls(body):
            cited.setdefault(norm(u), set()).add(ch)
        for line in lst.split('\n'):
            if not re.match(r'^\| \d+ \|', line):
                continue
            parts = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(parts) != 4:
                print('BADROW', p, line[:60])
                continue
            _, name, typ, url = parts
            k = norm(url)
            d = meta.setdefault(k, {'names': set(), 'types': set(), 'raws': set(), 'ch': set()})
            d['names'].add(name)
            d['types'].add(typ)
            d['raws'].add(url)
            d['ch'].add(ch)
    return meta, cited


def main():
    fb = io.open(FB, encoding='utf-8').read()
    gitems = global_list(fb)
    meta, cited = chapter_data()

    gmap = {}
    for n, s in gitems:
        us = [norm(u) for u in extract_urls(s)]
        key = us[0] if us else 'NOURL#%d' % n
        if len(us) > 1:
            print('MULTI-URL', n, s[:60], us)
        gmap[key] = (n, s)

    out = []
    out.append('全局条目=%d  正文被引 distinct=%d  清单元数据 distinct=%d'
               % (len(gitems), len(cited), len(meta)))
    out.append('\n## A. 全局清单有、正文未引用（%d）' % len([k for k in gmap if k not in cited]))
    for k, (n, s) in sorted(gmap.items(), key=lambda kv: kv[1][0]):
        if k not in cited:
            out.append('  #%d %s' % (n, s[:130]))
    out.append('\n## B. 正文引用、全局清单缺失（%d）' % len([k for k in cited if k not in gmap]))
    for k in sorted(cited):
        if k not in gmap:
            m = meta.get(k, {})
            names = ' / '.join(sorted(m.get('names', ['<无清单行>'])))
            types = ' / '.join(sorted(m.get('types', [])))
            out.append('  [%s] ch%s | %s | %s' % (k[:78], ','.join(sorted(m.get('ch', ['?']))), names[:60], types[:40]))
    out.append('\n## C. 元数据不一致（同名多类型或多名称）')
    for k, m in sorted(meta.items()):
        if len(m['types']) > 1 or len(m['names']) > 1:
            out.append('  %s' % k[:70])
            out.append('     names=%s' % sorted(m['names'])[:4])
            out.append('     types=%s' % sorted(m['types'])[:4])
    out.append('\n## D. 同一 URL 多种写法')
    for k, m in sorted(meta.items()):
        if len(m['raws']) > 1:
            out.append('  %s' % k[:70])
            out += ['     ' + r for r in sorted(m['raws'])]
    out.append('\n## E. 拟定终稿条目（按等级排序）')

    def tier_of(types):
        for t in types:
            m = re.search(r'S(\d)', t)
            if m:
                return int(m.group(1))
        return 9

    for k in sorted(cited, key=lambda k: (tier_of(meta.get(k, {}).get('types', [])), k)):
        m = meta.get(k)
        if not m:
            out.append('  [缺元数据] ch%s %s' % (','.join(sorted(cited[k])), k[:90]))
            continue
        name = max(sorted(m['names']), key=len)
        cnt = Counter(m['types'])
        typ = sorted(cnt, key=lambda t: (-cnt[t], -len(t), t))[0]
        out.append('  S%d | ch%s | %s | %s | %s' % (tier_of(m['types']),
                                                    ','.join(sorted(cited[k] | m['ch'])),
                                                    name[:70], typ[:34], k[:70]))
    io.open('_tools/_refs.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
    print('written _tools/_refs.txt')


if __name__ == '__main__':
    main()
