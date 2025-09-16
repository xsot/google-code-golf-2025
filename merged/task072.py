# joking (54 bytes, gold)
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[7:]+n)]or(a!=n)*3

### att (61 bytes)
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]

### combined (61 bytes)
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]

### ovs (62 bytes)
p=lambda g:[[3*(a!=b)for a,b in zip(*r)]for r in zip(g,g[7:])]
