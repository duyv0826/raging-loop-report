# 《人狼村之谜》深度研究报告：前置与后置框架

> 本文档为 Phase 5 终稿整合用的前置/后置框架，包含研究引言、目录、研究结论、参考文献四部分。终稿并入时，将引言置于第1章之前、目录置于引言之后、结论置于第6章之后、参考文献置于全文末尾。
> 跨章口径（终稿统一）：四主结局为一/二/三/四周目黄泉(Yomi)/机知(Wit)/暗黑(Darkness)/神明(Myth)，"第四主结局"即神明结局，Myth 统一译"神明"、不译"迷"；子阶段 Dense Mist 统一译"浓雾"、Infiltration 统一译"潜入"，"夕雾"仅保留于开场歌谣原文，不作为子阶段译名；「三車」系原作日文汉字，全篇统一以简体"三车家"表记，原作汉字与训读 みつむら 仅在第1章 1.1 首现处标注一次。

---

## 研究引言

**研究对象与缘起。** 《人狼村之谜》（日文原名『レイジングループ』，英文版名 *Raging Loop*，风格化写作 Rei-Jin-G-Lu-P，民间亦常略称"人狼村"）是由 KEMCO 出品、编剧 amphibian 执笔的一部轮回系视觉小说，2015 年于日本移动平台首发，其后登陆 Steam、PlayStation 4／Vita、Nintendo Switch 等平台，并有 iOS／Android 版本流通。作品以"人狼游戏"（现实版狼人杀）为骨架，将悬疑推理、民俗怪谈与多重轮回叙事编织为一体，在独立向视觉小说中以其严密的规则—叙事互锁结构而受到持续讨论。

**研究动机。** 选择本作作为深度研究对象的理由有三。其一，在轮回系（multiple-route／time-loop）视觉小说中，本作罕见地把"游戏规则"本身作为叙事推进的引擎：黄泉忌之宴的处刑规则、KEY 系统的解锁逻辑并非装饰，而是直接决定玩家能看见什么、相信什么。规则与叙事的互锁程度，值得专门剖析。其二，作品将桌游"狼人杀"现实化——活人成为棋子、处刑成为仪式——这种"游戏机制侵入现实"的设定，既是类型杂交的实验，也是对人狼博弈元隐喻的具象化。其三，作品在悬疑外壳之下承载了信仰即模因、信息操控、封闭社群人性实验、宗教批判与存在主义等主题，其思想成色远高于一般类型作，却也因结局密度与解释的递降而引发解读争议。系统梳理其设定、人物、结构、悬念、结局与主题，具有独立的研究价值。

**研究方法。** 本报告以公开网络资料的文献梳理与文本分析为主要方法：交叉比对百科类条目、媒体评测、玩家社区讨论与攻略站信息，并结合民间汉化版本的文本进行结构还原。凡涉及官方设定集、开发者访谈等一手资料之处，均标注来源；非官方整理内容（如社区推演的 KEY 链、结局触发条件）在文中以"待核实"或"玩家整理"注明。本报告不宣称具备考据学意义上的权威，而是一次面向中文读者的整合性文本研究。

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


**报告结构。** 全文由六章主体构成：第1章梳理故事背景与设定（休水村三重封闭、黄泉忌之宴规则、KEY 系统、章／周目结构）；第2章分析主要人物及其身份—关系—立场的三重错位；第3章按 Yomi／Wit／Darkness／Myth 四主线周目递进重述剧情；第4章拆解关键转折与"神→人→梦→叙述者"的解释权递降悬念工程；第5章汇总结局分支、触发条件与含义（4 主线＋26 坏结局＋2 替换结局）；第6章提炼贯穿作品的核心主题与隐喻。

**研究免责声明。** 本报告所有引用来源均为公开网络资料（百科、媒体评测、社区讨论、攻略站等），并非官方设定集或授权资料；部分事实在不同来源间存在冲突，或仅为玩家社区整理，文中已相应标注"待核实"。本作无官方简体中文版在大陆正规渠道流通，引用文本据民间汉化版本，译名以民间常用为准，并注明异译（如 Myth 作"神明"而非"迷"；长者四家之"三车家"全篇用简体表记，原作汉字「三車」仅首现处标注一次）。

---

## 目录

> 各章末统一附「本章引用来源清单」（含 S1–S7 来源等级）与「存疑与事实冲突说明」两节，因体例一致、不另列于目录。

- 研究引言
- 目录
- 第1章 故事背景与设定
  - 1.1 作品坐标
  - 1.2 地点：休水——雾里的行政末梢
    - 1.2.1 三重封闭
    - 1.2.2 社会结构：三层权力与三圈内外
  - 1.3 时间：现代日本，与覆盖其上的循环时间观
    - 1.3.1 现代性坐标
    - 1.3.2 村内的循环时间观
  - 1.4 核心规则：三层互锁的机制
    - 1.4.1 叙事层：黄泉忌之宴
    - 1.4.2 机制层：KEY 系统
    - 1.4.3 结构层：章／周目与导图
  - 1.5 本章小结：设定如何互锁
- 第2章 主要人物及其身份、关系与立场
  - 2.1 概览：人物即"角色扮演"
  - 2.2 人物关系总表
  - 2.3 主人公与"谜之少女"
  - 2.4 三车家与阴谋线核心
  - 2.5 村中关键村民与"高中生三人组"
  - 2.6 外来者与观察者
  - 2.7 阵营映射：理解人物关系的钥匙
  - 2.8 本章小结
- 第3章 主线剧情的分章与分阶段发展流程
  - 3.1 周目结构总览：剧本导图与 KEY 系统
  - 3.2 第1周目 · Yomi（黄泉）：初入村庄与死亡循环开启
  - 3.3 第2周目 · Wit（机知）：试探规则与人物——"赢了推理，仍被夺走一切"
  - 3.4 第3周目 · Darkness（暗黑）：阴谋浮出水面
  - 3.5 第4周目 · Myth（神明）：真相与核心解密
  - 3.6 关键事件流程时间线
  - 3.7 真相揭示的"信息增量"递进表
  - 3.8 引爆性质节点清单（预留第4章展开）
  - 3.9 本章小结：周目即信息进度
- 第4章 关键转折节点与核心悬念的逐层铺设
  - 4.1 论点：悬念结构不是"一个谜底"，而是一条"解释权递降的阶梯"
  - 4.2 论据一：四段抉择的骨架与线性锁
  - 4.3 论据二：三个最大转折点
  - 4.4 论据三：三车家真相的引爆点与伏笔收束
    - 4.4.1 芹泽千枝实的身份反转：从"盟友"到三车家血脉
    - 4.4.2 谜之少女／咩子的身份反转：羊型布偶与记忆保留者
  - 4.5 分析：悬念铺设的四种手法
  - 4.6 本章小结：降解与复魅交替的悬念工程
  - 4.7 关键发现
  - 4.8 数据摘要
- 第5章 结局分支及其触发条件与含义
  - 5.1 结局体系总览
  - 5.2 主线四结局：黄泉、机知、暗黑、神明
  - 5.3 26 个坏结局的主题分类与触发机制
  - 5.4 两个"替换结局"（暴露模式）的触发条件与主题意义
  - 5.5 真结局（神明结局）的达成路径：KEY 链与周目整合
  - 5.6 多结局设计意图：信息操控与真相的相对性
  - 5.7 本章小结
- 第6章 贯穿作品的核心主题与隐喻
  - 6.1 信仰即模因：被人为制造并操控的"神"
  - 6.2 信息操控与真相的相对性
  - 6.3 封闭社群与人性实验
  - 6.4 人狼游戏作为元隐喻
  - 6.5 对宗教迷信的批判、被讲述历史的质疑与存在主义色彩
  - 6.6 主题表达的可能争议
  - 6.7 本章小结
- 研究结论
- 参考文献

---

## 研究结论

《人狼村之谜》并非一部以"谁是狼人"为终极谜底的悬疑作，而是一套关于"人如何被给定的规则与叙事所塑造"的认知装置。将六章分析综合，可提炼出六条相互支撑的核心结论。

**其一，设定的互锁性。** 休水村的三重封闭——空间上被山与雾隔绝、社会上以三车家与黄泉忌之宴维持等级、认知上由怪谈与 KEY 系统限定可知边界——构成了一个自我闭合的信息容器。三重封锁并非并列布景，而是彼此咬合：空间封闭使社会规则不可外逸，社会规则使认知封锁具备强制力，认知封锁又反过来巩固空间与社会的封闭。作品的"谜"之所以有效，正因为谜面与谜底都被关在同一个容器里。

**其二，人物即角色扮演的三重错位。** 第2章指出，本作人物几乎都是"扮演者"：身份（你是谁）、关系（你与谁结盟）、立场（你为何行动）三者持续错位。房石阳明作为外来叙述者，其自我认知在轮回中不断被重写；三车家所代表的并非血缘实体而是权力符号；李花子、千枝实等角色在"被叙述"与"自我叙述"之间来回摆动。这种错位使人物成为叙事机制的节点，而非心理写实的对象。

**其三，轮回即叙事结构。** 第3章表明，四主线周目（Yomi／Wit／Darkness／Myth）并非重复，而是信息递进：每一周目解锁上一层规则，玩家可见的世界随之扩张。KEY 系统正是这一递进的物化——它把"你已理解多少"转化为可计量的进度。轮回在此不是宿命修辞，而是信息架构本身。

**其四，悬念工程即解释权递降。** 第4章拆解的"神→人→梦→叙述者"阶梯，是作品最精巧的设计：它把"谁在解释世界"一层层交出去，从神圣权威递降到凡人、再递降到梦境、最终落到不可靠的叙述者。每一次递降都重写了前一层悬念的含意，使"真相"成为一个随视角滑动的函数。

**其五，结局体系服务于信息操控主题。** 第5章汇总的 4 主线＋26 坏结局＋2 替换结局，并非单纯分支堆砌。KEY 链（Yomi→Key04，Wit→Key16，Darkness→Key20，Traitor#01→Key01→Myth）显示：真结局神话(Myth)的解锁，前提恰恰是玩家先遍历被操控的多数结局。结局的数量本身即是论证——你以为在选择，实则在被引导着走完信息操控的全套样本。

**其六，五大主题隐喻收束于认知装置的生成、运行与更替。** 信仰即模因说明"神"如何被复制；信息操控说明装置如何运行；封闭社群人性实验说明装置如何被试错；人狼元隐喻说明装置如何把人变成角色；宗教批判与存在主义（第6.6）则把装置推到更替的临界点——当叙述者也不再可靠，信仰便从"被给定"转为"被选择"。这正是作品的思想成色所在，也是其争议来源：它没有给出安放意义的终点，只交还了选择意义的责任。

综上，本作讲的不只是一场狼人杀，而是一套认知装置的生成、运行与更替——它让玩家在轮回中亲历"被规则塑造、被叙事欺骗、最终被迫自决"的全过程。这一结构上的自觉，使《人狼村之谜》在类型作品中具备值得反复进入的研究价值。

---

## 参考文献

> 下列 49 条为六章正文实际引用过的全部来源，按来源等级 S1→S7 编排（同级内按 URL 排序），每条标注类型等级、URL 与被引章节；编号与各章末「本章引用来源清单」相互对应，不重复计数。零引用的备查来源单列于本节末尾，未混入编号表。

1. Gematsu（转引官方站介绍与五眷属加护规则）. 官方一手·经转引降一档（英，S1→S2）. https://www.gematsu.com/2019/06/raging-loop-coming-west-for-ps4-switch-in-2019 〔第 1 章引用〕
2. Fandom Wiki: Endings. Wiki·可枚举（S2）. https://ragingloop.fandom.com/wiki/Endings 〔第 1、3、4、5 章引用〕
3. Raging Loop Fandom Wiki. Wiki/社区类（S2）. https://ragingloop.fandom.com/wiki/Raging_Loop 〔第 1、6 章引用〕
4. PSNProfiles: Raging Loop Text Guide. 文本攻略（英，S3）. https://forum.psnprofiles.com/topic/81654-raging-loop-text-guide/ 〔第 4、5 章引用〕
5. Knoef Raging Loop Trophy Guide. 奖杯攻略（英，S3）. https://knoef.info/trophy-guides/ps4-guides/raging-loop-trophy-guide 〔第 1、5、6 章引用〕
6. 雾雨小镇·【剧本】人狼村之谜（逐场景剧本转写）. 文本转写（中，S3）. https://www.mistytown.cn/forum.php?mod=viewthread&tid=11182 〔第 1–4 章引用〕
7. PSNine 奖杯列表. 奖杯数据（S3）. https://www.psnine.com/psngame/18014 〔第 3 章引用〕
8. ScorpioOfShadows: Raging Loop 攻略. 流程攻略（英，S3）. https://www.scorpioofshadows.com/post/raging-loop 〔第 1、3 章引用〕
9. VN Paths: Raging Loop Walkthrough and Guide. 流程攻略（英，S3）. https://vnpaths.com/raging-loop-walkthrough-and-guide/ 〔第 3–5 章引用〕
10. 网易·《人狼村之谜》评测：破圈的狼人杀与精彩的轮回系故事. 媒体评测（中，S4）. https://www.163.com/dy/article/FGRNNAQG05269PPR.html 〔第 2 章引用〕
11. GamingTrend·Raging Loop review. 媒体评测（英，S4）. https://gamingtrend.com/if-i-could-turn-back-time-raging-loop-review/ 〔第 1 章引用〕
12. 机核 GCORES《从〈人狼村之谜〉出发，窥见ACG作品中日本动物神明信仰的一角》. 媒体/文化考据类（S4）. https://www.gcores.com/articles/142710 〔第 4、6 章引用〕
13. 机核 GCORES·Steam游戏评测 第315期. 媒体评测（中，S4）. https://www.gcores.com/talks/1005995 〔第 2、3、5、6 章引用〕
14. TV Tropes: VisualNovel/RagingLoop. 媒体·trope 记录（S4）. https://tvtropes.org/pmwiki/pmwiki.php/VisualNovel/RagingLoop 〔第 4 章引用〕
15. VG 电玩帮／双鱼星鉴《陷入时间轮回的智斗神作》. 媒体分析（中，S4）. https://www.vgover.com/news/39034 〔第 3、5 章引用〕
16. 游研社·游戏库条目. 媒体资料（中，S4）. https://yystv.cn/g/1997 〔第 1 章引用〕
17. 游研社·玩了《人狼村之谜》，我变成了狼人模样. 媒体评测（中，S4）. https://yystv.cn/n/966150 〔第 1 章引用〕
18. 萌娘百科·人狼村之谜. 百科（中，S5）. https://zh.moegirl.org.cn/人狼村之谜 〔第 1–6 章引用〕（正文另见 zh.moegirl.tw、mobile.moegirl.org.cn/zh-hant 与百分号编码写法，同一条目）
19. 百度百科·人狼村之谜. 百科（中，S5）. https://baike.baidu.com/item/人狼村之谜/18841704 〔第 1、2 章引用〕
20. 快懂百科·人狼村之谜. 百科（中，S5）. https://www.baike.com/wikiid/3632591420506430650 〔第 1、4 章引用〕
21. Wikipedia: Mafia (party game). 百科类·英文（S5）. https://en.wikipedia.org/wiki/Mafia_(party_game) 〔第 6 章引用〕
22. Open Wiki: Raging Loop（英文 Wikipedia 派生镜像）. 百科镜像（S5）. https://www.owiki.org/wiki/Raging_Loop 〔第 4 章引用〕
23. Pinocchiopedia·Raging Loop（Miguruma clan）. 英文百科（S5）. http://pinocchiopedia.com/wiki/Raging_Loop 〔第 2 章引用〕
24. Reference.org《Raging Loop》条目（背景与前作提及）. 百科镜像（英，S5）. https://reference.org/facts/raging_loop/ItCUcBTA 〔第 1 章引用〕
25. Wikimili: Raging Loop（英文 Wikipedia 派生镜像）. 百科镜像（S5）. https://wikimili.com/en/Raging_Loop 〔第 4 章引用〕
26. Backloggd 玩家评论（Poketto）. 社区评论（S6）. https://backloggd.com/u/Poketto/reviews/recent:desc 〔第 4 章引用〕
27. JJwxc·人狼村之谜讨论（李花子/三车家争议）. 社区讨论（中，S6）. https://bbs.jjwxc.net/showmsg.php?board=3&boardpagemsg=37926&id=2536404 〔第 2 章引用〕
28. NGA 玩家讨论（周目与怪物梳理）. 社区讨论（S6）. https://bbs.nga.cn/read.php?page=1&tid=41652331 〔第 3 章引用〕
29. NGA·通关讨论（番外超能力争议）. 社区讨论（中，S6）. https://bbs.nga.cn/read.php?tid=39114781&page=2 〔第 2 章引用〕
30. 奶牛关·人狼村之谜评价（by 坡）. 社区评测（中，S6）. https://cowlevel.net/game/f724e450778327dc10647650167fdd1d/review/3994339 〔第 2 章引用〕
31. 3楼猫·人狼村之谜：破圈的狼人杀与精彩的轮回系故事. 社区长评（中，S6）. https://game.3loumao.org/81104 〔第 1 章引用〕
32. 机核 GCORES·速通打卡. 社区打卡（中，S6）. https://www.gcores.com/talks/1129770 〔第 2 章引用〕
33. Into Sanctuary 论坛《A Gauche Review / Production》剧情梳理. 社区讨论（S6）. https://intosanctuary.com/index.php?threads/raging-loop-a-gauche-review-production.922/ 〔第 3 章引用〕
34. AcFun·全结局＋番外＋暴露模式＋隐藏结局合集. 社区视频（中，S6）. https://m.acfun.cn/v/?ac=25276463 〔第 4、5 章引用〕
35. TapTap 玩家短评（结局数异说）. 社区评测（中，S6）. https://m.taptap.cn/moment/570026107928052538 〔第 1 章引用〕
36. NGA·朝花夕拾No.15 人狼村之谜. 社区讨论（中，S6）. https://nga.178.com/read.php?tid=22433268 〔第 2、5 章引用〕
37. NGA 一口气通了人狼村（含剧透）. 社区讨论（中，S6）. https://ngabbs.com/read.php?tid=31223780 〔第 2–4 章引用〕
38. Stage1st·《人狼村之谜》人物印象. 社区讨论（中，S6）. https://stage1st.com/2b/thread-2256040-1-1.html 〔第 2 章引用〕
39. TapTap 玩家评测（久岛鸥的旅行箱）. 社区评测（中，S6）. https://www.taptap.cn/moment/833459772937208388 〔第 1 章引用〕
40. 微博·人狼村之谜 repo（含剧透）. 社区随笔（中，S6）. https://weibo.com/ttarticle/p/show?id=2309405006092945195121 〔第 2、4 章引用〕
41. 斗鱼鱼吧·周目详解. 社区讨论（S6）. https://yubam.douyu.com/post/774168691675054042 〔第 3 章引用〕
42. 游戏星辰／2023game《全剧情解读》. 内容聚合（S7；仅在与 S3 级文本互证后作事实用）. https://www.2023game.com/sgame/cn/238275.html 〔第 3、4 章引用〕
43. 233乐园·内容攻略（规则与违规惩罚）. 下载／聚合站（中，S7）. https://www.233leyuan.com/post-detail/1956258247720419328 〔第 1、3 章引用〕
44. 街机站·设定考据（长者四家/伏良休主文字游戏）. 聚合站转载（中，S7）. http://www.jiejizhan.com/xz/27876.html 〔第 1、2 章引用〕
45. 开心电玩 kxdw（"20 个死亡结局"口径，事实冲突源）. 下载／聚合站（中，S7）. https://www.kxdw.com/android/170124.html 〔第 5 章引用〕
46. 4399 游戏（四结局通俗归纳：黄泉/机知/暗黑/神明）. 下载／聚合站（中，S7）. https://m.4399xyx.com/game/367097.html 〔第 5 章引用〕
47. 乐游网——首译"安水村". 下载页（中，S7）. https://m.962.net/mipy/618786.html 〔第 1 章引用〕
48. 游侠手游·周目结局（结局数异说）. 下载／聚合站（中，S7）. https://m.ali213.net/android/698571.html 〔第 1 章引用〕
49. 魔趣网《人狼村之谜》条目. 下载聚合（S7，仅作异说记录）. https://www.mfunz.com/game/15391.html 〔第 3 章引用〕

**未采信／备查来源（正文零引用，故不入编号表）**

- Anime News Network. (2019). Interview: Raging Loop scenario writer amphibian. https://www.animenewsnetwork.com/interview/2019-10-04/raging-loop-scenario-writer-amphibian/.151598 — S1 一手访谈，但本报告未能直接核对原文，全书涉及作者口径处均标注为"经 NGA 转述"，故不作事实来源，仅备查。
- MDPI Information. (2022). Information manipulation in narrative games. https://www.mdpi.com/2078-2489/13/3/134 — 学术旁证，六章正文从未据其立论，列入将构成虚引，移出。
- Digitally Downloaded. (2019). Raging Loop review. https://www.digitallydownloaded.net/2019/10/review-raging-loop-nintendo-switch.html — 英文评测，正文未引用（同类结论已由 GamingTrend、游研社支撑）。
- WCCFtech. (2019). Raging Loop review. https://wccftech.com/review/raging-loop-ps4-survive-the-feast-and-seek-the-truth/ — 英文评测，正文未引用。
- Bilibili专栏. (n.d.). 聊聊《人狼村之谜》神明一说. https://www.bilibili.com/read/cv15111400 — 视频专栏，正文未引用（Myth 译名口径另由 Fandom Endings 与中文站归纳支撑）。
- Bilibili专栏. (n.d.). 深度解析人狼村之谜. https://www.bilibili.com/read/cv14256601 — 视频专栏，正文未引用。
- Wikipedia contributors. (n.d.). Raging Loop. https://en.wikipedia.org/wiki/Raging_Loop — 正文未经此原件引用，仅引用其派生镜像（Open Wiki／Wikimili／Reference.org，见编号表 S5 段）；原件列此供溯源。

> URL 写法已统一：萌娘百科取 zh.moegirl.org.cn 简体汉字路径，百度百科取汉字路径，Wikipedia 保留成对括号的规范形式；正文中的百分号编码、.tw／zh-hant 镜像与 mobile 子域写法均指同一对象，已在对应条目注明。

---

*（本框架文档为前置／后置件，Phase 5 终稿整合时并入正文相应位置。六章正文已在本工作副本内按《00-conflict-rulings.md》的裁定完成改写，根目录原稿保持未动。）*
