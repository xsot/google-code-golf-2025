# ovs (134 vs 127 bytes for gold)
p=lambda g:[[sum({v}&{*r[:j]}|{*r[j:]}&{m[j],m[j:=j+1]})for v in m[2:]]for r in g if any(m:=[0,*min(g),j:=0])]or[*zip(*p([*zip(*g)]))]

### joking (151 bytes)
p=lambda g:[g:=[[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)]for E in[enumerate]*2][1]

## 
E=enumerate;p=lambda g:[g:=[[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)]for _ in g][1]

### combined (153 bytes)
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)

### att (176 bytes)
p=lambda a,n=-3:n*a or p([*map(lambda*b,i=0,n=[*map(min,a)]:[b:=[c*(m!=c in({*n}-{0}or b))for c in b[:i]]+[b[i]+(m in b[:i])*m,*b[(i:=i+1):]]for m in n[1:]][-1][::-1],*a)],n+1)
