# ovs (165 vs 156 bytes for gold)
p=lambda g,w=89,R=range(11):(W:=[[(g[r][c]==5)*5or(w%9<sum(v[c&12:][:3].count(a:=w//9)for v in g[r&12:][:3]))*a for c in R]for r in R])*(5!=a in sum(W,W))or p(g,w-1)

### joking (167 bytes)
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])==f[r//4+c//4*3])*sum({*sum(g,[-5])})for c in R]for r in R]

##
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])[r//4+c//4*3]//max(f)*sum({*sum(g,[-5])})for c in R]for r in R]

### combined (191 bytes)
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum([v[c:c+4]for v in g[r:r+4]],[]).count(C:=max({*sum(g,[])}-{5}))for c in[0,4,8]for r in[0,4,8]])==f[r//4+c//4*3])*C for c in R]for r in R]
