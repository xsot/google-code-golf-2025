# ovs (119 vs 99 bytes for gold)
E=enumerate
def p(g):a,*_,b={j%9:1for j,v in E(sum(g,[]))if v};return[[v%2*(j==a or(j==b)*2)for j,v in E(r)]for r in g]
