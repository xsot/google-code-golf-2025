# joking (153 bytes, gold)
p=lambda g,w=37,R=range(11),h=0:[[(g[r][c]==5)*5or(w<sum(t:=sum([*zip(*g[r&12:][:3])][c&12:][:3],()))>=(h:=1))*max(t)for c in R]for r in R]*h or p(g,w-1)


##
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])[r//4+c//4*3]//max(f)*sum({*sum(g,[-5])})for c in R]for r in R]
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])==f[r//4+c//4*3])*sum({*sum(g,[-5])})for c in R]for r in R]

### ovs (160 bytes)
p=lambda g,w=89,P=[],R=range(11):(W:=[[(g[r][c]==5)*5or(w%9<sum(v[c&12:][:3].count(w//9)for v in g[r&12:][:3]))*w//9for c in R]for r in R])*(W>P+g)or p(g,w-1,W)

### combined (191 bytes)
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum([v[c:c+4]for v in g[r:r+4]],[]).count(C:=max({*sum(g,[])}-{5}))for c in[0,4,8]for r in[0,4,8]])==f[r//4+c//4*3])*C for c in R]for r in R]
