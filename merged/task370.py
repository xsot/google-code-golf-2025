# compression_experiments (227 (357 unzipped) vs 159 bytes for gold)
def	p(r):
	for	i	in	range(4):t=[*map(min,r)].index(0);e=[*map(min,r)].count(0);r=[*map(list,zip(*r))][::-1];n=[*map(min,r)].index(0);[0for	i	in	range(4)for	o	in	range(e)for	s	in	range(e)for	r[n-1+r[n][t]//-9*~i-e*i-o][t-1+r[n][t]//-9*~i-e*i-s]in	r[n-1+r[n][t]//8][t-1+r[n][t]%8:][:1>r[n+o][t+s]<=n-1+r[n][t]//-9*~i-e*i-o|t-1+r[n][t]//-9*~i-e*i-s]]
	return	r

### joking (229 (357 unzipped) bytes)
def	p(g):
	for	s	in	range(4):x=[*map(min,g)].index(0);N=[*map(min,g)].count(0);g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0);[0for	s	in	range(4)for	i	in	range(N)for	j	in	range(N)for	g[y-1+g[y][x]//-9*~s-N*s-i][x-1+g[y][x]//-9*~s-N*s-j]in	g[y-1+g[y][x]//8][x-1+g[y][x]%8:][:1>g[y+i][x+j]<=y-1+g[y][x]//-9*~s-N*s-i|x-1+g[y][x]//-9*~s-N*s-j]]
	return	g

## zip parsing stuff
def p(g):
 for s in range(#[*range(4,41,4)]##):#[*perms('x=[*map(min,g)].index(0);N=[*map(min,g)].count(0)',';')]##;g=[*map(list,zip(*g))][::-1];y=[*map(min,g)].index(0);[#[*range(10)]##for s in range(#[prev_vals[0]]##)for i in range(N)for j in range(N)for g[y-1+g[y][x]//#['~8']##*~s-N*s-i][x-1+g[y][x]//#[prev_vals[-1]]##*~s-N*s-j]in g[y-1+g[y][x]//8][x-1+g[y][x]%8:][:1>g[y+i][x+j]<=y-1+g[y][x]//#[prev_vals[-1]]##*~s-N*s-i|x-1+g[y][x]//#[prev_vals[-1]]##*~s-N*s-j]]
 return g

### xsot (249 (358 unzipped) bytes)
# see ovs for uninlined version
def p(g,k=3):
 y=[*map(min,g)].index(0);x=[*map(min,*g)].index(0);N=[*map(min,*g)].count(0)
 for s in range(9):
  for i in range(N):
   for j in range(N):
    if-g[y+i][x+j]>-1<y+g[y][x]//-9*~s-N*s+~i|x+g[y][x]//-9*~s-N*s+~j:g[y+g[y][x]//-9*~s-N*s+~i][x+g[y][x]//-9*~s-N*s+~j]=g[y-1+g[y][x]//8][x-1+g[y][x]%8]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### ovs (255 (310 unzipped) bytes)
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

### mwi (269 (361 unzipped) bytes)
def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### combined (273 (342 unzipped) bytes)
def p(g,k=3):
 y,*_,Y=[y for y,r in enumerate(g)if 0in r];x,*_,X=[y for y,r in enumerate(zip(*g))if 0in r];h=Y+1-y;V=g[y][x];v=V>0
 for s in range(10):
  for i in range(h):
   for j in range(h):
    r=-s*(h-v)+v-1;a,b=y-i+r,x-j+r
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([[*r]for r in zip(*g[::-1])],k-1)
