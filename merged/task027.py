# joking (103 vs 97 bytes for gold)
p=lambda g,r=range(10):[[(g[i][j]^-g[C:=sum(map(max,*g,*zip(*g)))%2+~i][C+i-j])%3for j in r]for i in r]

### ovs (104 bytes)
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]

### combined (104 bytes)
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]
