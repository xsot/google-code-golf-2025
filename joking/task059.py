p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])==f[r//4+c//4*3])*sum({*sum(g,[-5])})for c in R]for r in R]

##
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])[r//4+c//4*3]//max(f)*sum({*sum(g,[-5])})for c in R]for r in R]