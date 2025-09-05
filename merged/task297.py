# combined (44 vs 2500 bytes for gold)
p=lambda i:i[:2]+[*zip(*[i[0]*2]*len(i[0]))]

### att (47 bytes)
p=lambda a:a[:2]+[[b]*len(a[0])for b in a[0]]*2

### ovs (47 bytes)
p=lambda g:g[:2]+[len(g[0])*[v]for v in g[0]*2]

### xsot (47 bytes)
p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]*2]
###
p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]]*2
