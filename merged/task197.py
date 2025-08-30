# att (54 bytes, gold)
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]

### combined (tied, 54 bytes)
p=lambda g:[[A[g[1].index(B)]for B in g[1]]for A in g]

### ovs (tied, 54 bytes)
p=lambda g:[[r[g[1].index(x)]for x in g[1]]for r in g]

### xsot (66 bytes)
p=lambda m:[[*map(dict([*zip(m[1],r)][::-1]).get,m[1])]for r in m]
##
p=lambda m:[[*map(dict([*zip(m[1],r)][::-1]).get,m[1])]for r in m]
p=lambda m:[[dict([*zip(m[1],r)][::-1])[i]for i in m[1]]for r in m]
p=lambda m:[[dict(zip(m[1][::-1],r[::-1]))[i]for i in m[1]]for r in m]
