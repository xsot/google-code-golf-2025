# combined (62 vs 2500 bytes for gold)
p=lambda i:[[-y%5^s*3for s,y in zip(*x)]for x in zip(i,i[5:])]

### att (63 bytes)
p=lambda a:[[3*c^b.pop(0)*3//2for c in a.pop(0)]for b in a[5:]]

### ovs (64 bytes)
p=lambda g:[[3*(v*2!=V)for v,V in zip(*r)]for r in zip(g,g[5:])]
