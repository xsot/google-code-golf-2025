# joking (58 vs 54 bytes for gold)
p=lambda i:[[any(y)*3for y in x]for x in map(zip,i,i[5:])]

### combined (60 bytes)
p=lambda i:[[any(y)*3for y in zip(*x)]for x in zip(i,i[5:])]

### att (61 bytes)
p=lambda a:[[c|b.pop(0)and 3for c in a.pop(0)]for b in a[5:]]

### ovs (63 bytes)
p=lambda g:[[v|V and 3for v,V in zip(*r)]for r in zip(g,g[5:])]
