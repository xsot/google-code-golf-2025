# ovs (75 vs 72 bytes for gold)
R=range(10)
p=lambda g:[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]

### combined (76 bytes)
p=lambda i,k=range(10):[[i[0][max(y,x)%(5-0**i[0][4])]for y in k]for x in k]
