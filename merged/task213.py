# combined (111 vs 92 bytes for gold)
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[k for k in i[0]if k]]or[*zip(*p([*zip(*i[::-1])]))][::-1]

### ovs (113 bytes)
def p(g):R=all(map(any,g));C={v:0 for r in[g,zip(*g)][R]for v in r if v%5};return[[[c,b][R]for b in C]for c in C]
