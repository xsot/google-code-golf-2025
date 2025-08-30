# combined (342 vs 320 bytes for gold)
def p(g,k=3):
 y,*_,Y=[y for y,r in enumerate(g)if 0in r];x,*_,X=[y for y,r in enumerate(zip(*g))if 0in r];h=Y+1-y;V=g[y][x];v=V>0
 for s in range(10):
  for i in range(h):
   for j in range(h):
    r=-s*(h-v)+v-1;a,b=y-i+r,x-j+r
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([[*r]for r in zip(*g[::-1])],k-1)
