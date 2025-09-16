# joking (53 bytes, gold)
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[5:]+n)]or 3>>a+n

### att (59 bytes)
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]

### combined (59 bytes)
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]

### ovs (61 bytes)
p=lambda g:[[3>>sum(x)for x in zip(*r)]for r in zip(g,g[5:])]

### xsot (61 bytes)
p=lambda m:[[3>>c+d for c,d in zip(*r)]for r in zip(m,m[5:])]
##
p=lambda m:[[3>>c+d for c,d in zip(m.pop(5),r)]for r in m[:4]]
p=lambda m:[[3-3*any(c)for c in zip(*r)]for r in zip(m,m[5:])]
p=lambda m:m[5:]and[[3-3*any(c)for c in zip(*m[::5])]]+p(m[1:])
p=lambda m:m[5:]and[[3-3*any(c)for c in zip(m.pop(0),m[4])]]+p(m)
