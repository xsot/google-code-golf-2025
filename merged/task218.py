# att (58 bytes, gold)
p=lambda a,*n:[*{b:0for b in zip(*n or p(a,*a))if any(b)}]

### joking+mwi (tied, 58 bytes)
p=lambda a,*n:[*{b:0for b in zip(*n or p(a,*a))if any(b)}]

### ovs (129 bytes)
u=lambda x:[i for i,v in enumerate(x)if v!=x[i-1]]
p=lambda g:[[f for j in u([*zip(*g)])if(f:=g[i][j])]for i in u(g)if any(g[i])]
