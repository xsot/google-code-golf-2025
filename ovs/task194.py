p=lambda g,a=-3:-a*g and[r:=g[a]+sum(g,[])[a::-3],*p(g,a+1),r[::-1]]
