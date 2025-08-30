def p(g):
 for y in(u:=range(1,h:=len(g)-1)):
  for x in u:
   c=g[y][x];A,B,C,D=[c==g[y+X//8-2][x+X%8-1]for X in b"	"];a,b,p,q=2*C-1,2*A-1,x,y
   while(A^B)*(C^D)*(g[y+a][x+b]^c)*c>0<p<h>q>0:q-=a;p-=b;g[q][p]=g[y+2*a][x+2*b]
 return g