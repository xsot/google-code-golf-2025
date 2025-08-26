u=lambda x:[i for i,v in enumerate(x)if v!=x[i-1]]
p=lambda g:[[f for j in u([*zip(*g)])if(f:=g[i][j])]for i in u(g)if any(g[i])]