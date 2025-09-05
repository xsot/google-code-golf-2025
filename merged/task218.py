# att (56 vs 2500 bytes for gold)
p=lambda a,*n:[*{b:0for b in zip(*n or p(*a))if any(b)}]

### combined (tied, 56 bytes)
p=lambda a,*n:[*{b:0for b in zip(*n or p(*a))if any(b)}]

### ovs (129 bytes)
u=lambda x:[i for i,v in enumerate(x)if v!=x[i-1]]
p=lambda g:[[f for j in u([*zip(*g)])if(f:=g[i][j])]for i in u(g)if any(g[i])]
