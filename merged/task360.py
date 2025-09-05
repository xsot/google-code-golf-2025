# att (45 vs 2500 bytes for gold)
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]

### ovs (tied, 45 bytes)
p=lambda g:[[*map(max,r,r[:4:-1])]for r in g]

### combined (tied, 45 bytes)
p=lambda i:[[*map(max,x,x[:4:-1])]for x in i]

### xsot (48 bytes)
p=lambda m:[[c|r.pop()for c in r[:4]]for r in m]
