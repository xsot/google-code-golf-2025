# ovs (104 vs 88 bytes for gold)
p=lambda g,q=0:[max(g[i],[(q:=q^v)>>v+1for r in g[:i]for v in(g[:i+1].count(r)<2)*r])for i in range(10)]
# [r for r in g[:i]if g[:i+1].count(r)<2] finds the row containing the relevant 4, 0, ..., 0, 4 sequence.
# There is probably a better way to construct the resulting rows with 2's from that

##
R=range(10)
p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in{*R}-{i}for J in{*R}-{j}})//5*2for j in R]for i in R]

### joking (114 bytes)
p=lambda g,R={*range(10)}:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in R^{i}for J in{j}^R})//5*2for j in R]for i in R]

##
exec("p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)"+"for %s in{*range(10)}%s"*4%('I','-{i}','J','-{j}})//5*2',*'j]i]'))

### combined (116 bytes)
p=lambda i,k=3:-k*i or p([[(y%2<=k)*(y or~-max({*x[:b],1}&{*x[b:],1}))for b,y in enumerate(x)]for x in zip(*i)],k-1)
