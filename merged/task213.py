# att (94 vs 92 bytes for gold)
p=lambda i:[*zip(*[u:=[*filter(int,w:=[sum({*r}-{5})for r in i])]]*len(u)*(u>w)or p(zip(*i)))]

### ovs (100 bytes)
p=lambda i:[*zip(*all(w:=[sum({*r}-{5})for r in i])and p([*zip(*i)])or[w:=[*filter(int,w)]]*len(w))]

##

p=lambda i:1%len(m:=max([[*{x:0for x in r if x%5}]for r in i],key=len))*[m]*len(m)or[*zip(*p([*zip(*i)]))]
p=lambda i:max([w:=r[j::3]]*len(w)*({*w}^{0,5}>{0,5,w[0]})for r in i for j in(0,1,2))or [*zip(*p([*zip(*i)]))]
def p(g):R=all(map(any,g));C={v:0 for r in[g,zip(*g)][R]for v in r if v%5};return[[[c,b][R]for b in C]for c in C]

### xsot (109 bytes)
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[*filter(int,i[0])]]or[*zip(*p([*zip(*i[::-1])]))][::-1]

### combined (111 bytes)
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[k for k in i[0]if k]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
