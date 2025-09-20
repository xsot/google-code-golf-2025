# mwi (204 bytes, gold)
def p(g):
 f=lambda C:{x+x//10*80for x in range(100)if C==g[x//10][x%10]};v=f(2)
 for y in f(0)|f(5):
  for Y in(m:=[Y+y-min(v)for Y in v])*(hash((*g[0],))%263+y!=99!={*m}<f(0)):g[Y//90][Y%90]=2
 return g

## no lambda
def p(g):
 z,v,V=[{x+x//10*80for x in range(100)if C==g[x//10][x%10]}for C in(0,2,5)]
 for y in z|V:
  for Y in(m:=[Y+y-min(v)for Y in v])*(hash((*g[0],))%263+y//90!=7!={*m}<z):g[Y//90][Y%90]=2;z-={Y}
 return g

## old version
def p(g):
 v=[[y,x]for y,r in enumerate(g)for x,c in enumerate(r)if c%5];i,j=min(v)
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   for Y,X in(1-(g[0]in[[0,5,5,5,5,0,0,5,y!=1,5],[0,5,5,5,0,0,x,5,5,5]]))*v*all(len(g[0])>X-j+x>-1<Y-i+y<len(g)and g[Y-i+y][X-j+x]<1for Y,X in v):g[Y-i+y][X-j+x]=2
 return g

### ovs (228 bytes)
E=enumerate
def p(g):
 z,v,V=[{(y,x)for y,r in E(g)for x,c in E(r)if c==C}for C in(0,2,5)];i,j=min(v)
 for y,x in z|V:
  for Y,X in(m:=[(Y-i+y,X-j+x)for Y,X in v])*(hash((*g[0],))%263+y!=7!={*m}<z):g[Y][X]=2;z-={(Y,X)}
 return g

### combined (238 (300 unzipped) bytes)
def p(g):
 e=enumerate;v=[[y,x]for y,r in e(g)for x,c in e(r)if c%5];i,j=min(v)
 for y,r in e(g):
  for x,c in e(r):
   if g[0]in[[0,5,5,5,5,0,0,5,y!=1,5],[0,5,5,5,0,0,x,5,5,5]]:continue
   for Y,X in v*all(len(g[0])>X-j+x>-1<Y-i+y<len(g)and g[Y-i+y][X-j+x]<1for Y,X in v):g[Y-i+y][X-j+x]=2
 return g
