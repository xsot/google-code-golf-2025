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
