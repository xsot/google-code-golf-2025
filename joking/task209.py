def	p(g):
	G=g
	for	s	in	G*4:G=[[*s]for	s	in	zip(*G[~4:])if{*s}-{0,4}];g=[[*s]for	s	in	zip(*g[(4in	g[-1])-2::-1])]
	for	s,r	in	enumerate(g):
		if[0for	y,r	in	enumerate(g)for	x,r	in	enumerate(s*r)for	Y,r	in	enumerate(s*all(g	in[0,((G+20*[[]])[(Y-y)//s]+20*[4])[(X-x)//s]]for	Y,g	in	enumerate(g)for	X,g	in	enumerate(g))*G)for	X,r	in	enumerate(s*r)for	g[Y+y][X+x]in[G[Y//s][X//s]]]:return	g

##
def p(g):
 G=g
 for s in G*4:G=[[*s]for s in zip(*G[#['~4','-5']##:])if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s,r in enumerate(g):
  if[#[*range(7)]##for y,r in enumerate(g)for x,r in enumerate(s*r)for Y,r in enumerate(s*all(g in[0,((G+#[*range(20,60)]##*[[]])[(Y-y)//s]+#[prev_vals[-1]]##*[4])[(X-x)//s]]for Y,g in enumerate(g)for X,g in enumerate(g))*G)for X,r in enumerate(s*r)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g