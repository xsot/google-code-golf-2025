def p(g,k=3):
 V=g[y:=[*map(min,g)].index(0)][x:=[*map(min,*g)].index(0)];N=[*map(min,*g)].count(0)
 for s in range(9):
  for i in range(N):
   for j in range(N):
    a=y+~i+V//-9*~s-N*s;b=x+~j+V//-9*~s-N*s
    if-g[y+i][x+j]>-1<a|b:g[a][b]=g[y-1+V//8][x-1+V%8]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

##

def p(g,k=3):
 *t,=map(min,*g);V=g[y:=[*map(min,g)].index(0)][x:=t.index(0)];N=t.count(0)
 for s in range(9*N*N):
  i=s//9;s%=9;h=V//-9*~s-N*s;a,b=y-i%N-1+h,x+~i//N+h
  if-g[y+i%N][x+i//N]>-1<a|b:g[a][b]=g[y-1+V//8][x-1+V%8]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
