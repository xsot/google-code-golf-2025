p=lambda g:[h[:5]for r in[*g]if(h:=g.pop()[::-1][[*r,1].index(1):])]

## recursive approach
p=lambda g,q=[]:g!=1and[p(s,t)for s,t in zip(g,(g+q)[::-1])if"1"in"%s"%s]or q