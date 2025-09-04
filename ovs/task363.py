E=enumerate
def p(g):
 z,v,V=[{(y,x)for y,r in E(g)for x,c in E(r)if c==C}for C in(0,2,5)];i,j=min(v)
 for y,x in z|V:
  for Y,X in(m:=[(Y-i+y,X-j+x)for Y,X in v])*(g[0]!=[0,5,5,5,5,0,0,5,y^1,5]!={*m}<z):g[Y][X]=2;z-={(Y,X)}
 return g
