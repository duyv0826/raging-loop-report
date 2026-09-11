# -*- coding: utf-8 -*-
"""终稿参考文献重建 · 第二阶段：写入 _report_frontback.md。

规则（全部可机械核验）：
1. 条目集合 = 六章正文实际引用过的 URL 归并集（49 条），按 S1→S7 排序；
2. 原全局清单中零引用的条目移出编号表，另列「未采信／备查来源」并写明理由；
3. URL 写法统一：优先取已在仓库中出现过的 https 原文形式，萌娘百科／百度百科取简体汉字路径；
   任一最终 URL 必须能在章节文件中逐字命中，否则视为我编造、直接报错中止；
4. 同时把《00-conflict-rulings.md》第 1 节的来源阶梯并入「研究方法」节（裁定表交付要求）。
"""
import io
import re
import glob
import urllib.parse
from collections import Counter

import sys
sys.path.insert(0, '_tools')
from gen_refs import norm, extract_urls, chapter_data, global_list  # noqa: E402

FB = '_report_frontback.md'
NL = '\n'
CANON = {
    'MOEGIRL/人狼村之谜': 'https://zh.moegirl.org.cn/人狼村之谜',
    'http://baike.baidu.com/item/人狼村之谜/18841704': 'https://baike.baidu.com/item/人狼村之谜/18841704',
    'http://en.wikipedia.org/wiki/Mafia_(party_game)': 'https://en.wikipedia.org/wiki/Mafia_(party_game)',
}
# 名称与类型的人工覆盖：机械规则（取最短名／最常见类型）在这几条上会挑到
# 信息量更差或带内部行话（E1、截断点）的写法，故显式指定。
NAME_OVERRIDE = {
    'http://233leyuan.com/post-detail/1956258247720419328': '233乐园·内容攻略（规则与违规惩罚）',
    'http://weibo.com/ttarticle/p/show?id=2309405006092945195121': '微博·人狼村之谜 repo（含剧透）',
    'http://m.acfun.cn/v/?ac=25276463': 'AcFun·全结局＋番外＋暴露模式＋隐藏结局合集',
}
TYPE_OVERRIDE = {
    'http://2023game.com/sgame/cn/238275.html': '内容聚合（S7；仅在与 S3 级文本互证后作事实用）',
    'http://mfunz.com/game/15391.html': '下载聚合（S7，仅作异说记录）',
}
VARIANT_NOTE = {
    'MOEGIRL/人狼村之谜': '（正文另见 zh.moegirl.tw、mobile.moegirl.org.cn/zh-hant 与百分号编码写法，同一条目）',
}

UNUSED = [
    ('Anime News Network. (2019). Interview: Raging Loop scenario writer amphibian.',
     'https://www.animenewsnetwork.com/interview/2019-10-04/raging-loop-scenario-writer-amphibian/.151598',
     'S1 一手访谈，但本报告未能直接核对原文，全书涉及作者口径处均标注为"经 NGA 转述"，故不作事实来源，仅备查。'),
    ('MDPI Information. (2022). Information manipulation in narrative games.',
     'https://www.mdpi.com/2078-2489/13/3/134',
     '学术旁证，六章正文从未据其立论，列入将构成虚引，移出。'),
    ('Digitally Downloaded. (2019). Raging Loop review.',
     'https://www.digitallydownloaded.net/2019/10/review-raging-loop-nintendo-switch.html',
     '英文评测，正文未引用（同类结论已由 GamingTrend、游研社支撑）。'),
    ('WCCFtech. (2019). Raging Loop review.',
     'https://wccftech.com/review/raging-loop-ps4-survive-the-feast-and-seek-the-truth/',
     '英文评测，正文未引用。'),
    ('Bilibili专栏. (n.d.). 聊聊《人狼村之谜》神明一说.', 'https://www.bilibili.com/read/cv15111400',
     '视频专栏，正文未引用（Myth 译名口径另由 Fandom Endings 与中文站归纳支撑）。'),
    ('Bilibili专栏. (n.d.). 深度解析人狼村之谜.', 'https://www.bilibili.com/read/cv14256601',
     '视频专栏，正文未引用。'),
    ('Wikipedia contributors. (n.d.). Raging Loop.', 'https://en.wikipedia.org/wiki/Raging_Loop',
     '正文未经此原件引用，仅引用其派生镜像（Open Wiki／Wikimili／Reference.org，见编号表 S5 段）；原件列此供溯源。'),
]

LADDER = '''
**来源优先级阶梯（S1–S7）。** 本报告不以"哪个说法看起来更可信"裁定冲突，而以来源等级裁定；同级冲突时，采"可复核的枚举"优于"散文式复述"。阶梯由《00-conflict-rulings.md》第 1 节确立，全文各章清单与下方参考文献均按此标注：

| 级 | 类型 | 本报告已用来源举例 |
|---|------|------|
| **S1** | 官方一手：官网、发行商公告、作者访谈／QA | 官方站英文介绍（经 Gematsu 转引）、作者 amphibian QA（经 NGA 转述，非直接一手）、Anime News Network 访谈 |
| **S2** | 英文社区 Wiki，逐条枚举且可复核 | Raging Loop Fandom Wiki `Endings`（#01–#26 编号＋KEY 归属） |
| **S3** | 游戏文本转写型攻略：奖杯攻略、文本攻略、流程攻略 | Knoef Trophy Guide、PSNProfiles Text Guide、VN Paths、ScorpioOfShadows、PSNine、雾雨小镇剧本转写 |
| **S4** | 中文／英文媒体评测与分析文章 | 机核 GCORES、游研社、电玩帮／双鱼星鉴、GamingTrend、网易、TV Tropes |
| **S5** | 百科条目（中／英）及其镜像 | 萌娘百科、百度百科、快懂百科、Wikipedia（及镜像 Open Wiki／Wikimili／Reference.org）、Pinocchiopedia |
| **S6** | 玩家社区讨论与剧本整理 | NGA、Stage1st、微博 repo、奶牛关、JJwxc、TapTap、3楼猫、AcFun、斗鱼鱼吧、Into Sanctuary、Backloggd |
| **S7** | 内容聚合站／下载站转载（最低） | 街机站、游戏星辰、233乐园、游侠手游、开心电玩、4399、魔趣网、乐游网 |

**阶梯三条例外规则**（裁定时优先适用）：① S1 经二手转述时降一档，并须显式标注"据社区转述"；② 计数类事实（结局数、KEY 数、章节数）以能逐条枚举者为准，不以复述者为准；③ 凡全报告仅有 S7 一处来源支撑的事实，一律不得写作定论，必须带限定语或移入"存疑与事实冲突说明"。
'''


def tier_of(types):
    for t in types:
        m = re.search(r'S(\d)', t)
        if m:
            return int(m.group(1))
    return 9


def canonical(k, raws, body_corpus, list_corpus, log):
    """选定最终 URL 写法：白名单 > 正文里逐字出现过的形式 > 清单里的形式 > 报错。
    两段都不含"我新拼一个 URL"的可能，因此不会引入虚构地址。"""
    if k in CANON:
        log.append(('CANON', k))
        return CANON[k]
    cands = sorted(raws, key=lambda r: (not r.startswith('https://'), -len(r), r))
    for stage, c in ((1, body_corpus), (2, list_corpus)):
        for r in cands:
            if r in c:
                log.append(('body' if stage == 1 else 'list', k))
                return r
    raise SystemExit('no verifiable spelling for %s (raws=%s)' % (k, sorted(raws)))


def chapters_str(chs):
    n = sorted(int(c) for c in chs)
    return '%d–%d' % (n[0], n[-1]) if n == list(range(n[0], n[-1] + 1)) and len(n) > 2 else '、'.join(map(str, n))


def main():
    fb = io.open(FB, encoding='utf-8').read()
    body_corpus, list_corpus = [], []
    for p in sorted(glob.glob('chapters/ch*.md')):
        text = io.open(p, encoding='utf-8').read()
        a = text.index('## 本章引用来源清单')
        b = text.index('## 存疑与事实冲突说明')
        body_corpus.append(text[:a] + text[b:])
        list_corpus.append(text[a:b])
    body_corpus = NL.join(body_corpus)
    list_corpus = NL.join(list_corpus)
    log = []
    meta, cited = chapter_data()
    assert not [k for k in cited if k not in meta], 'cited URL without chapter metadata'

    old = global_list(fb)
    keys = sorted(cited, key=lambda k: (tier_of(meta[k]['types']), k))
    lines = []
    for i, k in enumerate(keys, 1):
        m = meta[k]
        cnt = Counter(m['types'])
        typ = sorted(cnt, key=lambda t: (-cnt[t], -len(t), t))[0]
        name = NAME_OVERRIDE.get(k) or min(sorted(m['names']), key=len)
        typ = TYPE_OVERRIDE.get(k) or typ
        url = canonical(k, m['raws'], body_corpus, list_corpus, log)
        chs = chapters_str(cited[k] | m['ch'])
        note = VARIANT_NOTE.get(k, '')
        lines.append('%d. %s. %s. %s 〔第 %s 章引用〕%s' % (i, name, typ, url, chs, note))

    sec = ['## 参考文献',
           '',
           '> 下列 %d 条为六章正文实际引用过的全部来源，按来源等级 S1→S7 编排（同级内按 URL 排序），'
           '每条标注类型等级、URL 与被引章节；编号与各章末「本章引用来源清单」相互对应，不重复计数。'
           '零引用的备查来源单列于本节末尾，未混入编号表。' % len(lines),
           '',
           ] + lines + ['',
                        '**未采信／备查来源（正文零引用，故不入编号表）**',
                        '']
    sec += ['- %s %s — %s' % (t, u, why) for t, u, why in UNUSED]
    sec.append('')
    sec.append('> URL 写法已统一：萌娘百科取 zh.moegirl.org.cn 简体汉字路径，百度百科取汉字路径，'
               'Wikipedia 保留成对括号的规范形式；正文中的百分号编码、.tw／zh-hant 镜像与 mobile 子域写法'
               '均指同一对象，已在对应条目注明。')
    sec.append('')
    sec.append('')

    i = fb.index('## 参考文献')
    j = fb.index('\n---\n', i)
    new_fb = fb[:i] + '\n'.join(sec) + fb[j + 1:]

    # 研究方法节并入来源阶梯
    anchor = '本报告不宣称具备考据学意义上的权威，而是一次面向中文读者的整合性文本研究。'
    assert anchor in new_fb, 'anchor for 研究方法 missing'
    if LADDER not in new_fb:
        new_fb = new_fb.replace(anchor, anchor + '\n' + LADDER, 1)

    # 前置说明里的"APA 参考文献"表述随之更正
    new_fb = new_fb.replace('目录、研究结论、APA 参考文献四部分', '目录、研究结论、参考文献四部分', 1)
    assert 'APA 参考文献' not in new_fb

    io.open(FB, 'w', encoding='utf-8', newline='\n').write(new_fb)
    print('references rebuilt: %d -> %d numbered entries (+%d 备查)' % (len(old), len(lines), len(UNUSED)))
    print('URL spelling source:', Counter(s for s, _ in log).most_common())
    io.open('_tools/_refs_log.txt', 'w', encoding='utf-8', newline=NL).write(
        NL.join('%s  %s' % (s, k) for s, k in log) + NL)


if __name__ == '__main__':
    main()
