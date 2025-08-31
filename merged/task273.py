# combined (116 bytes, gold)
p=lambda i,k=3:-k*i or p([[(y%2<=k)*(y or~-max({*x[:b],1}&{*x[b:],1}))for b,y in enumerate(x)]for x in zip(*i)],k-1)

### ovs (tied, 116 bytes)
R=range(10)
p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in{*R}-{i}for J in{*R}-{j}})//5*2for j in R]for i in R]
