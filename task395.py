p=lambda m:[[2*(m[i][j]+m[i+3][j]<1)for j in[0,1,2]]for i in[0,1,2]]
###
p=lambda m:[[2*(u[j]+v[j]<1)for j in[0,1,2]]for u,v in zip(m,m[3:])]
p=lambda m:[[1>>u[j]+v[j]<<1for j in[0,1,2]]for u,v in zip(m,m[3:])]
p=lambda m,r=range(3):[[2*(m[i][j]+m[i+3][j]<1)for j in r]for i in r]