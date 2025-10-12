p=lambda g,w=37,R=range(11),h=0:[[(g[r][c]==5)*5or(w<sum(t:=sum([*zip(*g[r&12:][:3])][c&12:][:3],()))>=(h:=1))*max(t)for c in R]for r in R]*h or p(g,w-1)


##
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])[r//4+c//4*3]//max(f)*sum({*sum(g,[-5])})for c in R]for r in R]
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])==f[r//4+c//4*3])*sum({*sum(g,[-5])})for c in R]for r in R]