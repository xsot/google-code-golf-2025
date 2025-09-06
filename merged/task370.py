# ovs (269 (357 unzipped) bytes, gold)
def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8][x-1+V%8]
 return-k*g or p([*map(list,zip(*g))][::-1],k-1)

##

R=range
def p(g,k=3):
 T,t=[[0in r for r in w]for w in(g,zip(*g))];V=g[y:=T.index(1)][x:=t.index(1)];N=sum(t)
 for s in R(9):
  for i in R(N):
   for j in R(N):
    h=V//-9*~s-N*s;a,b=y+~i+h,x+~j+h
    if-g[y+i][x+j]>-1<a|b:g[a][b]=g[y-1+V//8][x-1+V%8]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### mwi (tied, 269 (361 unzipped) bytes)
def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### combined (276 (342 unzipped) bytes)
def p(g,k=3):
 y,*_,Y=[y for y,r in enumerate(g)if 0in r];x,*_,X=[y for y,r in enumerate(zip(*g))if 0in r];h=Y+1-y;V=g[y][x];v=V>0
 for s in range(10):
  for i in range(h):
   for j in range(h):
    r=-s*(h-v)+v-1;a,b=y-i+r,x-j+r
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([[*r]for r in zip(*g[::-1])],k-1)
