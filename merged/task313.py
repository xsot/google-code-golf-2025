# ovs (74 vs 63 bytes for gold)
p=lambda g,k=1:-k*g or p(([*zip(*g)][k:len({*g[0]})-1+k]*99)[:len(g)],k-1)
