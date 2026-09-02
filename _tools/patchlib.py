"""Apply rulings to chapter files by line-range replacement.

Anchoring on line numbers (verified against an expected substring) is safer than
long exact-string matches here, because the source uses full-width ASCII quote
characters that are easy to transcribe wrong. A mismatched expectation aborts the
whole run without writing, so a stale anchor can never produce a silent partial edit.

Each patch: {"ln": [start, end], "has": "...", "new": "..."}  -- start/end inclusive, 1-based.
"""
import sys, io


def apply(fname, patches):
    with io.open(fname, encoding='utf-8') as f:
        lines = f.read().split('\n')

    plan = []
    ok = True
    for i, p in enumerate(patches):
        a, b = p['ln']
        block = '\n'.join(lines[a - 1:b])
        frag = p['has']
        if frag not in block:
            print('MISS  %s[%d] ln=%d-%d expected substring not found: %r'
                  % (fname, i, a, b, frag[:50]))
            ok = False
            continue
        plan.append((a, b, p['new'], p.get('insert_after', False)))
        print('OK    %s[%d] ln=%d-%d %s %s'
              % (fname, i, a, b, 'INSERT' if p.get('insert_after') else 'REPL  ', frag[:44]))

    if not ok:
        print('--- %s: aborted, nothing written' % fname)
        return False

    for a, b, new, ins in sorted(plan, key=lambda t: (t[0], t[1]), reverse=True):
        block = new.split('\n') if new != '' else []
        if ins:
            lines[b:b] = block
        else:
            lines[a - 1:b] = block

    with io.open(fname, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('--- %s: %d edits written' % (fname, len(plan)))
    return True


if __name__ == '__main__':
    all_ok = True
    for spec in sys.argv[1:]:
        ns = {}
        with io.open(spec + '.py', encoding='utf-8') as f:
            exec(compile(f.read(), spec + '.py', 'exec'), ns)
        if not apply(ns['FILE'], ns['PATCHES']):
            all_ok = False
    sys.exit(0 if all_ok else 1)
