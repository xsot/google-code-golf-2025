# joking (172 vs 160 bytes for gold)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)

##
p=lambda i,k=39,z=0:-k*[r:=range(len({*sum(i,[])})-1)]and[[(y==x)*8for y in r]for x in r]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
p=lambda i,k=39,r=0,z=0:-k*[[(y==x)*8for y in r]for x in r]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1,range(len({*sum(i,[])})-1))
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h*[s,s:=h]+[0])or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)

### combined (tied, 172 bytes)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)

### xsot (258 (293 unzipped) bytes)
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
