# att (122 vs 117 bytes for gold)
z=[[0]*10]
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+'for*a,in map(zip,z+a,a,a,a[1:]+z)]'*2)

### joking+mwi (tied, 122 bytes)
z=[[0]*10]
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+'for*a,in map(zip,z+a,a,a,a[1:]+z)]'*2)
