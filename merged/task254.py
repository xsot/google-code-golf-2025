# joking (95 vs 84 bytes for gold)
def p(i):k=*zip(*i),;return[[x.pop(0)>>(s!=max(k))+2*(s!=sorted({*k})[1])for s in k]for x in i]

### mwi (99 bytes)
def p(i):k=*zip(*i),;return[[y and(s==max(k))+2*(s==sorted({*k})[1])for y,s in zip(x,k)]for x in i]

### combined (103 bytes)
def p(i):k=*map(sum,zip(*i)),;return[[y and s//max(k)+min({*k}-{0})//s*2for y,s in zip(x,k)]for x in i]

### ovs (119 bytes)
E=enumerate
def p(g):a,*_,b={j%9:1for j,v in E(sum(g,[]))if v};return[[v%2*(j==a or(j==b)*2)for j,v in E(r)]for r in g]
