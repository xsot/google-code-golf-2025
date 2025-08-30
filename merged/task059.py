# combined (191 vs 156 bytes for gold)
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum([v[c:c+4]for v in g[r:r+4]],[]).count(C:=max({*sum(g,[])}-{5}))for c in[0,4,8]for r in[0,4,8]])==f[r//4+c//4*3])*C for c in R]for r in R]

### ovs (tied, 191 bytes)
def p(g):f=sum(g,[]);C=[sum(R[i%11&~3:][:4].count(0)for R in g[i//11&~3:][:4])for i in range(121)];return[[v*(v==5)or(C[i]==min(C))*max({*f}-{5})for i,v in r]for r in zip(*[enumerate(f)]*11)]
