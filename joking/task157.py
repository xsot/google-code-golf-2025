# zip fiddling
def	p(g):
	r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
	for	l	in	range(t%15+16-w):
		for	s	in	1,0:
			u=*map(list,g),
			for	x	in	g[6:]:
				s+=any(x[t:w])
				for	b	in	range(t,w):g[s][b-t+l]+=x[b]>4;x[b]=0
			g=p(g)or	u
	if{*g[1]+g[2]}=={1,2}:return	g

##
def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(t%15#['+16-w','-w+16']##):
  for s in #['1,0','0,1']##:
   u=*map(list,g),
   for x in g[6:]:
    s+=any(x[t:w])
    for b in range(t,w):g[s][b-t+l]+=#['x[b]>4','4<x[b]']##;x[b]=0
   g=p(g)or u
 if{*#['g[1]+g[2]','g[2]+g[1]']##}=={#['1,2','2,1']##}:return g