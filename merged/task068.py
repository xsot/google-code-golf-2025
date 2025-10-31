# ovs (103 vs 99 bytes for gold)
p=lambda a,k=6,q=0:~k*a or p([[[2*q,v][q:=sum(a,r).count(v)<9-k]for v in r]for*r,in zip(*a)][::-1],k-2)

### joking (115 bytes)
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]\nfor*a,in map(zip,a[:1]+a,a,a,a[1:]+a)]#'*2)

### att (119 bytes)
s='for*a,in map(zip,[s]+a,a,a,a[1:]+[s])]'
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+s*2)

### combined (122 bytes)
z=[[0]*10]
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+'for*a,in map(zip,z+a,a,a,a[1:]+z)]'*2)
