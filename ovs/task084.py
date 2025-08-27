def p(g,i=0):
 while g[1-i:]:i-=1;g[~i][i]=2;g[-1][i]=4
 return g