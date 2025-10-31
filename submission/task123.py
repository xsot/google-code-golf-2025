R=range(10)
p=lambda g:[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]