p=lambda g,w=89,R=range(11):(W:=[[(g[r][c]==5)*5or(w%9<sum(v[c&12:][:3].count(a:=w//9)for v in g[r&12:][:3]))*a for c in R]for r in R])*(5!=a in sum(W,W))or p(g,w-1)
