# att (62 vs 55 bytes for gold)
p=lambda a,i=2:[p(b,4)for*b,in map(zip,a,a[i:])]or max(max(a))

##
p=lambda a:[*map(f:=lambda*b:[*map(max,b,b[-3:])],*map(f,*a))]
p=lambda a:[a:=[*zip(*map(map,[max]*3,a,a[-3:]))]for _ in a][1]
p=lambda a,*n:[[*map(max,b,b[-3:])]for b in zip(*n or p(a,*a))]
p=eval('lambda a:[[max(max(a))'+'for*a,in map(zip,a,a[-3:])]'*2)

### ovs (63 bytes)
p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]

### combined (63 bytes)
p=lambda i:[[*map(max,x,s,x[4:],s[4:])]for x,s in zip(i,i[2:])]

### xsot (85 bytes)
p=lambda m:[[max(max(m))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]
##
p=lambda m:[[max(sum(m,[]))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]
