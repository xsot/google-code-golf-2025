def p(g,F=0):
 for W in 3,3,2:
  for i in range(h:=len(g)):
   for j in range(w:=len(g[0])):
    X=[(i+k*d,j+k*D)for k in range(W+1)for d,D in((0,1),(0,-1),(1,0),(-1,0))];V=[not h>I>-1<J<w or g[I][J]for I,J in X];N=sum([r[max(0,j+~W):j+W+2]for r in g[max(0,i+~W):i+W+2]],[])
    for I,J in{*X*all(V)*(2in V[W%2*-4:]or F)*(V[3:].count(2)==N.count(2)>1<8>max(N))}:
     if h>I>-1<J<w:F=g[I][J]=2+g[I][J]%2*6
 return g
