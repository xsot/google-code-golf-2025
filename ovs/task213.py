p=lambda i:[*zip(*all(w:=[sum({*r}-{5})for r in i])and p([*zip(*i)])or[w:=[*filter(int,w)]]*len(w))]

##

p=lambda i:1%len(m:=max([[*{x:0for x in r if x%5}]for r in i],key=len))*[m]*len(m)or[*zip(*p([*zip(*i)]))]
p=lambda i:max([w:=r[j::3]]*len(w)*({*w}^{0,5}>{0,5,w[0]})for r in i for j in(0,1,2))or [*zip(*p([*zip(*i)]))]
def p(g):R=all(map(any,g));C={v:0 for r in[g,zip(*g)][R]for v in r if v%5};return[[[c,b][R]for b in C]for c in C]
