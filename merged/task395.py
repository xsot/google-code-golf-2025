# combined (56 vs 2500 bytes for gold)
p=lambda a:[[2-c-b.pop(0)&6for c in a.pop(3)]for b in a]

### att (57 bytes)
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(3)]for b in a]

### ovs (61 bytes)
p=lambda g:[[a-9+b&2for a,b in zip(*r)]for r in zip(g,g[3:])]

### xsot (63 bytes)
p=lambda m:[[2*(i+j<1)for i,j in zip(*u)]for u in zip(m,m[3:])]

###
p=lambda m:[[2*(i+j<1)for i,j in zip(*u)]for u in zip(m,m[3:])]
p=lambda m:[[2*(i+j<1)for i,j in zip(u,v)]for u,v in zip(m,m[3:])]
p=lambda m:[[2*(m[i][j]+m[i+3][j]<1)for j in[0,1,2]]for i in[0,1,2]]
p=lambda m:[[2*(u[j]+v[j]<1)for j in[0,1,2]]for u,v in zip(m,m[3:])]
p=lambda m:[[1>>u[j]+v[j]<<1for j in[0,1,2]]for u,v in zip(m,m[3:])]
p=lambda m,r=range(3):[[2*(m[i][j]+m[i+3][j]<1)for j in r]for i in r]
