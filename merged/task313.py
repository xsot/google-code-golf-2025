# joking+mwi (65 vs 63 bytes for gold)
p=lambda g,x=1:[(g[x:=x^1][1:len({*g[0]})]*9)[:len(g)]for _ in g]

### ovs (74 bytes)
p=lambda g,k=1:-k*g or p(([*zip(*g)][k:len({*g[0]})-1+k]*99)[:len(g)],k-1)
