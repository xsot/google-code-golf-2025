def p(g):g=eval(str(g).replace(*'04'));[g:=[[v%(q+4)for v,q in zip(r,[0]+r)]for*r,in zip(*g)][::-1]for _ in g*4];return g

### xsot (264 bytes)
def p(m):
 N=len(m:=eval(str(m).replace(*'04')))
 for i in range(N*N):
  q=(m[r:=i//N][c:=i%N]==4>1>c%~-N*(r%~-N))*[(r,c)]
  while q:
   m[r][c]=0;(y,x),*q=q
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
    if-1<i<N>j>-1<4==m[i][j]:m[i][j]=0;q+=(i,j),
 return m
