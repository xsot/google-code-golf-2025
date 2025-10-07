def	p(g):
	t=S=i=0
	while	g[i:]:
		if	g[0]<g[i]:
			t=t	or	g[i:].index(g[0]);s={(o,O)for	o	in	range(i,i+t)for	O	in	range(10)if	g[o][O]};S=S	or	s;o,O=next((o,O)for	O	in(0,-1,1,2)for	o	in	range(i)if(A:={(h-o,H-O)for	h,H	in	s	if-1<H-O<10})<=S)
			for	h,H	in	S-A:
				if-1<H--O<10:g[o+h][H--O]=1
			i+=t-1
		i+=1
	return	g

##
def p(g):
 #[*perms('S=t=i','=')]##=0
 while g[i:]:
  if g[0]<g[i]:
   t=t or g[i:].index(g[0])#[';','\n   ']##s={(o,O)for o in range(i,i+t)for O in range(10)if g[o][O]}#[';','\n   ']##S=S or s#[';','\n   ']##o,O=next((o,O)for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S)
   for h,H in S-A:
    if-1<H--O<10:g[o+h][H--O]=1
   i+=t-1
  i+=1
 return g