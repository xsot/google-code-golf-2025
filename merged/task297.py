p=lambda a:a[:2]+[[b]*len(a[0])for b in a[0]]*2

### ovs (tied, 47 bytes)
p=lambda g:g[:2]+[len(g[0])*[v]for v in g[0]*2]

### xsot (tied, 47 bytes)
p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]*2]
###
p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]]*2
