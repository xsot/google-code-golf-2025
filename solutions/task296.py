p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]

### xsot (85 bytes)
p=lambda m:[[max(max(m))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]
##
p=lambda m:[[max(sum(m,[]))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]
