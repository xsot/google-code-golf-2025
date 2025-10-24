p=lambda g,q=0:g and[max(g[0],[(q:=q^v)>>v+1for r in g[1:]for v in(g.count(r)<2)*r])]+p(g[1:])
