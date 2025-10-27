# compression_experiments (228 (357 unzipped) bytes, gold)
def	p(a):
	for	f	in	range(4):m=[*map(min,a)].index(0);i=[*map(min,a)].count(0);a=[*map(list,zip(*a))][::-1];u=[*map(min,a)].index(0);[0for	f	in	range(4)for	d	in	range(i)for	n	in	range(i)for	a[u-1+a[u][m]//-9*~f-i*f-d][m-1+a[u][m]//-9*~f-i*f-n]in	a[u-1+a[u][m]//8][m-1+a[u][m]%8:][:1>a[u+d][m+n]<=u-1+a[u][m]//-9*~f-i*f-d|m-1+a[u][m]//-9*~f-i*f-n]]
	return	a

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
