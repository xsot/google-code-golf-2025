# ovs (76 vs 2500 bytes for gold)
R=range(10)
p=lambda g:[[g[0][max(i,j)%(5-0**g[0][4])]for j in R]for i in R]

### combined (tied, 76 bytes)
p=lambda i,k=range(10):[[i[0][max(y,x)%(5-0**i[0][4])]for y in k]for x in k]
