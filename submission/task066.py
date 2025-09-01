def p(g):
 def p(y,x,A,B,V,g,C=0,G=0):
  if(len(g)>x>-1<y<len(g))*16<=C+13|G:return
  if(t:=g[y][x])==2:
   for i,j in V:g[i][j]=3
   return
  if t>7:
   for D,E in[[B,A],[-B,A],[B,-A],[-B,-A]]*G:p(y-A+D,x-B+E,D,E,{*V,(y-A,x-B)},g,C+1)
   return
  p(y+A,x+B,A,B,{*V,(y,x)},g,C,G+1)
 for(A,B),(C,D)in(X:=[(A,B)for A,C in enumerate(g)for B,D in enumerate(C)if g[A][B]==3]),X[::-1]:p(C+C-A,D+D-B,C-A,D-B,X,g)
 return g