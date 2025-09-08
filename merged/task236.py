# att (61 vs 54 bytes for gold)
p=lambda a:[[3*c^-b.pop(0)%5for c in a.pop(0)]for b in a[5:]]

### combined (62 bytes)
p=lambda i:[[-y%5^s*3for s,y in zip(*x)]for x in zip(i,i[5:])]

### ovs (64 bytes)
p=lambda g:[[3*(v*2!=V)for v,V in zip(*r)]for r in zip(g,g[5:])]
