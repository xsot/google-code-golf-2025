def p(g):
 for i in range(len(g)):g[i][i]=g[-i-1][i]=0
 return g