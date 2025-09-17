# mwi (275 (322 unzipped) vs 268 bytes for gold)
# zip-optimized version of ovs's 277
def	p(g):
	M={A*1j+g:y	for	A,C	in	enumerate(g)for	g,y	in	enumerate(C)};A,C=[y	for	y	in	M	if	M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
	for*V,y,A,C,G	in	S:
		if(y	in	M)*16>G|C+13:
			for	y	in(M[y]==2)*V:g[int(y.imag)][int(y.real)]=3
			F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for	D	in[A][F:]or[A*1j,A/1j]*G]
	return	g

##
def p(g):
 def p(y,x,A,B,V,g,C=0):
  if C>2:return
  for G in range(20):
   if not len(g[0])>x>-1<y<len(g)or(y,x)in V:break
   if(t:=g[y][x])==2:
    for i,j in V:g[i][j]=3
    return
   if t>7:
    for D,E in(G>0)*[[B,A],[-B,A],[B,-A],[-B,-A]]:p(y-A+D,x-B+E,D,E,{*V,(y-A,x-B)},g,C+1)
    break
   V=V|{(y,x)};y+=A;x+=B
 (C,D),(A,B)=[[A,B]for A,C in enumerate(g)for B,D in enumerate(C)if g[A][B]==3];H={(C,D),(A,B)};p(C+C-A,D+D-B,C-A,D-B,H,g);p(A+A-C,B+B-D,A-C,B-D,H,g);return g

### ovs (277 (322 unzipped) bytes)
def p(g):
 M={A*1j+B:D for A,C in enumerate(g)for B,D in enumerate(C)};A,C=[y for y in M if M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
 for*V,y,A,C,G in S:
  if(y in M)*16>G|C+13:
   for y in(M[y]==2)*V:g[int(y.imag)][int(y.real)]=3
   F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for D in[A][F:]or[A*1j,A/1j]*G]
 return g

### combined (346 (479 unzipped) bytes)
def p(g):
 def F(y,x,A,B,V,g,C=0):
  if C>2:return
  for G in range(20):
   if not len(g[0])>x>-1<y<len(g)or(y,x)in V:break
   if(t:=g[y][x])==2:
    for i,j in V:g[i][j]=3
    return
   if t>7:
    if G:
     for(D,E)in[[B,A],[-B,A],[B,-A],[-B,-A]]:F(y-A+D,x-B+E,D,E,{*V,(y-A,x-B)},g,C+1)
    break
   V=V|{(y,x)};y+=A;x+=B
 E=enumerate;(C,D),(A,B)=[[A,B]for(A,C)in E(g)for(B,D)in E(C)if g[A][B]==3];H={(C,D),(A,B)};F(C+C-A,D+D-B,C-A,D-B,H,g);F(A+A-C,B+B-D,A-C,B-D,H,g);return g
