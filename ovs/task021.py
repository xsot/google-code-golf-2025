H=lambda w:1+min(map(w.count,w))
p=lambda g:[g[0][:1]*H(g[0])]*H(g)