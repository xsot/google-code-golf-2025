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