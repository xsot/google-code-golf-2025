# ovs (113 vs 92 bytes for gold)
def p(g):R=all(map(any,g));C={v:0 for r in[g,zip(*g)][R]for v in r if v%5};return[[[c,b][R]for b in C]for c in C]
