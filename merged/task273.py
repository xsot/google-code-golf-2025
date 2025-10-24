# ovs (90 vs 88 bytes for gold)
p=lambda g,q=0:g and[max(g[:1]+[[2&(q:=q^v)>>v+g.count(r)for v in r]for r in g])]+p(g[1:])

### joking (114 bytes)
p=lambda g,R={*range(10)}:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in R^{i}for J in{j}^R})//5*2for j in R]for i in R]

##
exec("p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)"+"for %s in{*range(10)}%s"*4%('I','-{i}','J','-{j}})//5*2',*'j]i]'))

### combined (116 bytes)
p=lambda i,k=3:-k*i or p([[(y%2<=k)*(y or~-max({*x[:b],1}&{*x[b:],1}))for b,y in enumerate(x)]for x in zip(*i)],k-1)
