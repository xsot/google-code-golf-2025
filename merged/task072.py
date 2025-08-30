# att (61 vs 54 bytes for gold)
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]

### ovs (62 bytes)
p=lambda g:[[3*(a!=b)for a,b in zip(*r)]for r in zip(g,g[7:])]
