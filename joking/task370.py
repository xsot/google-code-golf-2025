# sorry, not sorry
def p(g):
 N=[*map(min,g)].count(0)
 x=[*map(min,g)].index(0)
 g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0)
 for s in range(7):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 N=[*map(min,g)].count(0)
 x=[*map(min,g)].index(0)
 g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0)
 for s in range(7):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 N=[*map(min,g)].count(0)
 x=[*map(min,g)].index(0)
 g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0)
 for s in range(7):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 N=[*map(min,g)].count(0)
 x=[*map(min,g)].index(0)
 g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0)
 for s in range(7):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 return g

## recursive version for +3b
def p(g,k=2):
 x=[*map(min,g)].index(0)
 N=[*map(min,g)].count(0);g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0)
 for s in range(9):
  for i in range(N):
   for j in range(N):
    if 1>g[y+i][x+j]<=y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 return-k*g or p(g,k-1)

## zip parsing stuff
def p(g):
 #[r'''#[(t1:='x=[*map(min,g)].index(0)')+(t2:='''#['\n ']##''')+(t3:='N=[*map(min,g)].count(0)'),t3+t2+t1]###[';','\n ']##g=[*map(list,zip(*g))][::-1]#[';','\n ']##y=[*map(min,g)].index(0)
 for s in range(#[*range(4,10)]##):
  for i in range(N):
   for j in range(N):
    if#['-g[y+i][x+j]>-1<',' 1>g[y+i][x+j]<=']##y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 '''*4]##return g

def p(g,k=2):
 x=[*map(min,g)].index(0)#[';','\n ']##N=[*map(min,g)].count(0)#[';','\n ']##g=[*map(list,zip(*g))][::-1]#[';','\n ']##y=[*map(min,g)].index(0)
 for s in range(#[*range(4,10)]##):
  for i in range(N):
   for j in range(N):
    if#['-g[y+i][x+j]>-1<',' 1>g[y+i][x+j]<=']##y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y+g[y][x]//8-1][x+g[y][x]%8-1]
 return-k*g or p(g,k-1)