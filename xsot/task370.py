# see ovs for uninlined version
def p(g,k=3):
 y=[*map(min,g)].index(0);x=[*map(min,*g)].index(0);N=[*map(min,*g)].count(0)
 for s in range(9):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y-1+g[y][x]//8][x-1+g[y][x]%8]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)