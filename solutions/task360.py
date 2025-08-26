p=lambda g:[[*map(max,r,r[:4:-1])]for r in g]

### xsot (48 bytes)
p=lambda m:[[c|r.pop()for c in r[:4]]for r in m]
