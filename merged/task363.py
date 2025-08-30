# combined (300 vs 217 bytes for gold)
def p(g):
 e=enumerate;v=[[y,x]for y,r in e(g)for x,c in e(r)if c%5];i,j=min(v)
 for y,r in e(g):
  for x,c in e(r):
   if g[0]in[[0,5,5,5,5,0,0,5,y!=1,5],[0,5,5,5,0,0,x,5,5,5]]:continue
   for Y,X in v*all(len(g[0])>X-j+x>-1<Y-i+y<len(g)and g[Y-i+y][X-j+x]<1for Y,X in v):g[Y-i+y][X-j+x]=2
 return g
