# combined (103 vs 99 bytes for gold)
def p(i):k=*map(sum,zip(*i)),;return[[y and s//max(k)+min({*k}-{0})//s*2for y,s in zip(x,k)]for x in i]

### ovs (119 bytes)
E=enumerate
def p(g):a,*_,b={j%9:1for j,v in E(sum(g,[]))if v};return[[v%2*(j==a or(j==b)*2)for j,v in E(r)]for r in g]
