# joking+mwi (96 vs 90 bytes for gold)
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)

### ovs (tied, 96 bytes)
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)
