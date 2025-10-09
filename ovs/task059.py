p=lambda g,w=89,P=[],R=range(11):(W:=[[(g[r][c]==5)*5or(w%9<sum(v[c&12:][:3].count(w//9)for v in g[r&12:][:3]))*w//9for c in R]for r in R])*(W>P+g)or p(g,w-1,W)
