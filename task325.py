def p(m,R=range):
 z=0;M,N=len(m),len(m[0])
 for i in R(M*N):
  z+=(b:=m[r:=i//N][c:=i%N]>0)
  s=[];q=b*[(r,c)]
  while q:
   (y,x),*q=q;s+=(y,x),
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]*(m[y][x]>0):
    if M>i>-1<j<N:q+=(i,j),
   m[y][x]=0
 return[[8*(r==c)for c in R(z)]for r in R(z)]