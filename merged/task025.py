# combined (153 bytes, gold)
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)

### ovs (tied, 153 bytes)
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)

### att (176 bytes)
p=lambda a,n=-3:n*a or p([*map(lambda*b,i=0,n=[*map(min,a)]:[b:=[c*(m!=c in({*n}-{0}or b))for c in b[:i]]+[b[i]+(m in b[:i])*m,*b[(i:=i+1):]]for m in n[1:]][-1][::-1],*a)],n+1)
