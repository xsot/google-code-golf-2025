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

## not optimized for compression, 320/358:
E=enumerate
def p(g):
 def p(y,A,V,g,C=0,G=0):
  if({y}<{*M})*16>G|C+13>1>((t:=M[y])==2!=[0for i,g[int(i.imag)][int(i.real)]in zip(V,[3]*99)]):F=t>7;y-=A*F;W=A*1j-A.imag*2;[p(y+D,D,{*V,y},g,C+F,~-F*~G)for D in[A][F:]or[W,A*1j,A/1j,W]*G]
 M={A*1j+B:D for A,C in E(g)for B,D in E(C)};X=[K for K in M if M[K]==3];[p(C+C-A,C-A,X,g)for A,C in(X,X[::-1])];return g
