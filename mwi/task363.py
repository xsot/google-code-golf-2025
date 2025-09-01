def p(g):
 v=[[y,x]for y,r in enumerate(g)for x,c in enumerate(r)if c%5];i,j=min(v)
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   for Y,X in(1-(g[0]in[[0,5,5,5,5,0,0,5,y!=1,5],[0,5,5,5,0,0,x,5,5,5]]))*v*all(len(g[0])>X-j+x>-1<Y-i+y<len(g)and g[Y-i+y][X-j+x]<1for Y,X in v):g[Y-i+y][X-j+x]=2
 return g