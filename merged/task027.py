# ovs (104 vs 103 bytes for gold)
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]
