def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)