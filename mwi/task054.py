# zip-optimized version of ovs's 284
def p(g):
 f=sum(g,[]);*C,p,B=sorted({*f},key=f.count);M={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={i for i in M for I in M if abs(I-i)==1}
 for i in{*M}-T:
  for I in T:
   d=I-sum(T)/len(T);g[int(I.imag)][int(I.real)]=B;F=1;p=I;I=d+i
   while(g[int(I.imag)][int(I.real)]^B)*F:g[int(I.imag)][int(I.real)]=M[p];I+=d/2;F-=abs(d)<2
 return g


##
def p(g):
 f=sum(g,[]);*C,p,B=sorted({*f},key=f.count);M={(i,I):J for(i,j)in enumerate(g)for(I,J)in enumerate(j)if J in C};T={(i,j)for(i,j)in M for(I,J)in M if(I-i)**2+(J-j)**2==1}
 for(i,j)in{*M}-T:
  for(I,J)in T:
   y,x=zip(*T);d=I-sum(y)//len(y);D=J-sum(x)//len(x);g[I][J]=B;F=1
   while((r:=g[d+i])[D+j]^B)*F:r[D+j]=M[I,J];d+=(d>0)-(d<0);D+=(D>0)-(D<0);F-=-3<d|D<3
 return g
## alt
def p(g):
 B=enumerate;K=sum(g,[]);*R,C,A=sorted({*K},key=K.count);L=max(G for(E,D)in B(g)for(F,G)in B(D[:-1])if G!=A!=C==D[F+1]);I,J=max([E,F]for(E,D)in B(g)for(F,G)in B(D[:-1])if g[E][F]==L!=A!=D[F+1]!=C!=D[F-1]!=A)
 for(F,G)in[[E,F]for(E,D)in B(g)for(F,G)in B(D[:-1])if G==L!=C==D[F+1]]:
  for Q in range(9):
   if g[I+Q//3-1][J+Q%3-1]-A:g[F+Q//3-1][G+Q%3-1]=g[I+Q//3-1][J+Q%3-1]
  for Q in range(9):
   N,O=Q%3-1,Q//3-1;D,E=N*2,O*2;P=g[I+D][J+E]
   while(N+O)*(C!=P!=A<len(g[0])>G+E>-1<F+D<len(g)>g[F+D][G+E]!=A):g[F+D][G+E]=P;D+=N;E+=O
 for Q in range(25):g[I-2+Q//5][J-2+Q%5]=A
 return g