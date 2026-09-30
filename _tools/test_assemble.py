# -*- coding: utf-8 -*-
"""assemble.py 的回归测试（全在 scratch 副本里跑，绝不碰仓库里的终稿）。

钉住四条这次踩过或容易再踩的性质：
① 正常路径：自检通过并落盘，三块后置附录在位，六章体例计数不变
② 幂等：连跑两次产物字节一致（终稿只能由源文件决定）
③ 内部工作指代回潮即拒绝落盘（《事实核查报告》在 BAN 名单里）
④ 写盘中段崩（磁盘满／后续 assert 炸）不得把交付稿截断成半截，
   也不得留下 .tmp；备份 _backup_prev_* 允许存在并由人工清理。

跑法：仓库根目录下 `python _tools/test_assemble.py`，全绿时末行打印 ALL PASS。
"""
import io
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(REPO, '_tools', '_scratch_repo')
OUT = '终稿_人狼村之谜研究报告.md'
FB = '_report_frontback.md'
POST = ('附：玩家社区声音（2026-09，一手自述）',
        '附录 A　事实核验补充记录（2026-09-30 复核）',
        '附录 B　30 秒实机自证操作（暴露模式）')
TAIL = '> 说明：若无实机条件，可用 2 张对照截图（普通模式 vs 暴露模式同一段落）替代演示；截图中红色文本框可见即可。'
SKIP = {'.git', '__pycache__', '_scratch_repo'}
fails = []


def setup():
    if os.path.isdir(DST):
        shutil.rmtree(DST)
    shutil.copytree(REPO, DST, ignore=shutil.ignore_patterns(*SKIP))


def run(script, args=None):
    return subprocess.run([sys.executable] + [script] + (args or []), cwd=DST,
                          capture_output=True)


def read(name):
    return io.open(os.path.join(DST, name), encoding='utf-8', newline='').read()


def patch(fname, old, new):
    p = os.path.join(DST, fname)
    t = io.open(p, encoding='utf-8', newline='').read()
    assert old in t, (fname, old)
    io.open(p, 'w', encoding='utf-8', newline='').write(t.replace(old, new, 1))


def ok(cond, label):
    if not cond:
        fails.append(label)


# ① 正常路径
setup()
r = run('_tools/assemble.py')
ok(r.returncode == 0, '① rc=%d: %s' % (r.returncode, r.stdout.decode('utf-8', 'replace')))
doc = read(OUT)
ok(all(('## ' + h) in doc for h in POST), '① 三块后置附录缺失')
ok(doc.count('## 本章引用来源清单') == 6, '① 本章引用来源清单 %d' % doc.count('## 本章引用来源清单'))
ok(doc.count('## 存疑与事实冲突说明') == 6, '① 存疑与事实冲突说明 %d' % doc.count('## 存疑与事实冲突说明'))
ok(doc.rstrip('\n').split('\n')[-1] == TAIL, '① 末行非附录 B 收尾句')
ok(os.path.isfile(os.path.join(DST, '_tools', '_verify.txt')), '① verify_final 未在 scratch 留下 _verify.txt')

# ② 幂等
h1 = read(OUT)
run('_tools/assemble.py')
ok(read(OUT) == h1, '② 重跑产物发生变化')
ok(read(FB).count('## ' + POST[0]) == 1, '② 前置件内附录标题重复')

# ③ 内部工作指代回潮
setup()
before = read(OUT)
patch(FB, '## ' + POST[2], '## 《事实核查报告》' + POST[2])
r = run('_tools/assemble.py')
ok(r.returncode != 0, '③ 内部引用回潮却落盘成功')
ok(read(OUT) == before, '③ 拒绝落盘时仍改写了终稿')

# ④ 写盘中段崩
setup()
before = read(OUT)
probe = os.path.join(DST, '_tools', '_probe.py')
shutil.copy(os.path.join(DST, '_tools', 'assemble.py'), probe)
t = io.open(probe, encoding='utf-8', newline='').read()
io.open(probe, 'w', encoding='utf-8', newline='').write(
    t.replace('        os.replace(tmp, OUT)', "        raise OSError('probe')\n        os.replace(tmp, OUT)", 1))
r = run('_tools/_probe.py')
ok(r.returncode == 2, '④ rc=%d 应为 2' % r.returncode)
ok('WRITE ABORTED' in r.stdout.decode('utf-8', 'replace'), '④ 未打印 WRITE ABORTED')
ok(read(OUT) == before, '④ 交付稿被截断或改写')
ok(not os.path.isfile(os.path.join(DST, OUT + '.tmp')), '④ 残留 .tmp')

print('FAILURES:', fails)
if fails:
    print('scratch kept for debugging:', DST)
    sys.exit(1)
shutil.rmtree(DST, ignore_errors=True)
print('ALL PASS')
