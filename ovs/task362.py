p=lambda g:[r[(n:=g.count(g[0])):9]+r[:1]+r[:n]for r in g*2][10-n:-n]
