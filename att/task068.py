s='for*a,in map(zip,[s]+a,a,a,a[1:]+[s])]'
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+s*2)