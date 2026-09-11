# -*- coding: utf-8 -*-
# Step 3 (统一模板) — ch01/ch03 only.
# 目标模板：编号正文 → ## N.x 本章小结 → ## 本章引用来源清单 → ## 存疑与事实冲突说明
import io

E1 = 'https://www.mistytown.cn/forum.php?mod=viewthread&tid=11182'
TIER_NOTE = '''> 各条目的来源等级（S1–S7）依《00-conflict-rulings.md》第 1 节的阶梯判定；终稿参考文献统一标注。'''

SPECS = {}

# ---------------- ch01 ----------------
SPECS['ch01'] = ('chapters/ch01.md', [
    {'ln': [121, 121], 'has': '## 1.5 小结：设定如何互锁', 'new': '''## 1.5 本章小结：设定如何互锁'''},
    {'ln': [131, 131], 'has': '## 存疑与待核实事项汇总', 'new': '''## 存疑与事实冲突说明'''},
    # R-11 同步：存疑表中的"官方汉字表记"表述
    {'ln': [139, 139], 'has': '官方汉字表记"乐境虏逋"', 'new': '''| 译名 | "休水"vs"安水"；"黄泉忌之宴"vs"黄泉忌闭之宴"；汉字表记"乐境虏逋"（官方抑或民间所造未核实） | 全报告统一用"休水""黄泉忌之宴"，首次出现加注异译；"乐境虏逋"不作 Wit 译名 |'''},
    # 消除 17b 这一编号遗留：自下而上重编 17/17b/18/19 → 17/18/19/20
    {'ln': [166, 166], 'has': '| 17b |', 'new': '''| 18 | 雾雨小镇·【剧本】人狼村之谜（逐场景剧本转写：四家职能、机知线收束、怀柔政策与供品、能里家笔记） | 文本转写（中，S3） | https://www.mistytown.cn/forum.php?mod=viewthread&tid=11182 |'''},
    {'ln': [167, 167], 'has': '| 18 | 乐游网', 'new': '''| 19 | 乐游网——首译"安水村" | 下载页（中，S7） | https://m.962.net/mipy/618786.html |'''},
    {'ln': [168, 168], 'has': '| 19 | Reference.org', 'new': '''| 20 | Reference.org《Raging Loop》条目（背景与前作提及） | 百科镜像（英文，S5） | https://reference.org/facts/raging_loop/ItCUcBTA |'''},
])

# ---------------- ch03 ----------------
CH03_SOURCES = '''## 本章引用来源清单

| # | 来源 | 类型（阶梯） | URL |
|---|------|------|-----|
| 1 | Fandom Wiki: Endings（四主线／坏结局编号与 KEY 归属） | Wiki·可枚举（S2） | https://ragingloop.fandom.com/wiki/Endings |
| 2 | 雾雨小镇·【剧本】人狼村之谜（逐场景剧本转写） | 文本转写（S3） | https://www.mistytown.cn/forum.php?mod=viewthread&tid=11182 |
| 3 | VN Paths: Raging Loop Walkthrough and Guide | 流程攻略（S3） | https://vnpaths.com/raging-loop-walkthrough-and-guide/ |
| 4 | ScorpioOfShadows: Raging Loop 攻略 | 流程攻略（S3） | https://www.scorpioofshadows.com/post/raging-loop |
| 5 | PSNine 奖杯列表 | 奖杯数据（S3） | https://www.psnine.com/psngame/18014 |
| 6 | 机核 GCORES《Steam游戏评测 第315期〈人狼村之谜〉》 | 媒体评测（S4） | https://www.gcores.com/talks/1005995 |
| 7 | VG 电玩帮／双鱼星鉴《陷入时间轮回的智斗神作》 | 媒体评测（S4） | https://www.vgover.com/news/39034 |
| 8 | 萌娘百科《人狼村之谜》 | 百科（S5） | https://mobile.moegirl.org.cn/zh-hant/%E4%BA%BA%E7%8B%BC%E6%9D%91%E4%B9%8B%E8%B0%9C |
| 9 | NGA [朝花夕拾No.15]／一口气通了人狼村 | 社区讨论（S6） | https://nga.178.com/read.php?tid=22433268 ；https://ngabbs.com/read.php?tid=31223780 |
| 10 | NGA 玩家讨论（周目与怪物梳理） | 社区讨论（S6） | https://bbs.nga.cn/read.php?page=1&tid=41652331 |
| 11 | Into Sanctuary 论坛《A Gauche Review / Production》剧情梳理 | 社区讨论（S6） | https://intosanctuary.com/index.php?threads/raging-loop-a-gauche-review-production.922/ |
| 12 | 斗鱼鱼吧·周目详解 | 社区讨论（S6） | https://yubam.douyu.com/post/774168691675054042 |
| 13 | 游戏星辰／2023game《全剧情解读》 | 内容聚合（S7） | https://www.2023game.com/sgame/cn/238275.html |
| 14 | 233乐园·设定梳理 | 内容聚合（S7） | https://www.233leyuan.com/post-detail/1956258247720419328 |
| 15 | 魔趣网《人狼村之谜》条目 | 下载聚合（S7，仅作截断点记录） | https://www.mfunz.com/game/15391.html |

'''

CH03_DOUBTS = '''## 存疑与事实冲突说明

- **已消解**：3.3 机知线"存活离村后全村已死"与"千枝实自杀、主角跳崖"二说，经与逐场景剧本转写比对，确认是同一收束序列的第 4～6 步与第 3～6 步，**非互斥异说**；原"来源存在分歧、建议以游戏本体为准"的处理已删除。
- **口径区分**：3.1 的"约 20 个 KEY"（机核评测口径）与第5章的"26 个坏结局"（Fandom 枚举）是两个不同指标；中文站"20 个死亡结局"一说与前者数字巧合，易被误读为同一件事。
- **未核实项**：咩子（黑山羊幼崽）与羊型布偶"绵羊"是否同一存在，剧本转写未点明，本章按两者分述，不作定论。
- **降级引用**：Into Sanctuary 与魔趣网在本章仅作为"截断点如何产生"的记录被引用，不同场景下的具体死法一律以 E1 剧本转写为准。
- **表记与译名**：Myth 统一译"神明"（不译"迷"）；Dense Mist＝浓雾、Infiltration＝潜入；"夕雾"仅见于开场歌谣；三车家全篇用简体。'''

SPECS['ch03'] = ('chapters/ch03.md', [
    {'ln': [126, 126], 'has': '## 3.9 小结', 'new': '''## 3.9 本章小结：周目即信息进度'''},
    {'ln': [122, 122], 'has': '以科学/逻辑瓦解迷信、说服村民停手', 'insert_after': True,
     'new': '''> 落点核对：上述五项在第4章的释放位置依次为 **4.4**（狼爷爷）、**4.4.1**（千枝实＝三车血脉）、**4.3 转折点②＋4.4.2**（绵羊／咩子）、**4.4.2**（李花子＝巨型怪物）、**4.3 转折点③**（天谜地解）。本章预告与第4章实际内容已逐项对齐，无承诺未兑现项。'''},
    {'ln': [128, 128], 'has': '下一章将聚焦上述"引爆点"是如何被逐层铺设并集中释放的', 'insert_after': True,
     'new': '\n---\n\n' + CH03_SOURCES + TIER_NOTE + '\n\n---\n\n' + CH03_DOUBTS},
])

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '_tools')
    from patchlib import apply
    ok = True
    for key in ('ch01', 'ch03'):
        fname, patches = SPECS[key]
        if not apply(fname, patches):
            ok = False
    sys.exit(0 if ok else 1)
