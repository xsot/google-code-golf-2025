# joking+mwi (76 vs 75 bytes for gold)
p=lambda i,k=range(10):[[i[0][max(y,x)%(5-0**i[0][4])]for y in k]for x in k]

### ovs (tied, 76 bytes)
R=range(10)
p=lambda g:[[g[0][max(i,j)%(5-0**g[0][4])]for j in R]for i in R]
