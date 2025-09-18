# joking (115 bytes, gold)
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]\nfor*a,in map(zip,a[:1]+a,a,a,a[1:]+a)]#'*2)

### att (119 bytes)
s='for*a,in map(zip,[s]+a,a,a,a[1:]+[s])]'
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+s*2)

### combined (122 bytes)
z=[[0]*10]
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+'for*a,in map(zip,z+a,a,a,a[1:]+z)]'*2)
