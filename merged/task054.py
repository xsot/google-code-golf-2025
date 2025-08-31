# combined (381 (589 unzipped) vs 356 bytes for gold)
def p(g):
 B=enumerate;K=sum(g,[]);*R,C,A=sorted({*K},key=K.count);L=max(G for(E,D)in B(g)for(F,G)in B(D[:-1])if G!=A!=C==D[F+1]);I,J=max([E,F]for(E,D)in B(g)for(F,G)in B(D[:-1])if g[E][F]==L!=A!=D[F+1]!=C!=D[F-1]!=A)
 for(F,G)in[[E,F]for(E,D)in B(g)for(F,G)in B(D[:-1])if G==L!=C==D[F+1]]:
  for Q in range(9):
   if g[I-1+Q//3][J-1+Q%3]-A:g[F-1+Q//3][G+1-Q%3]=g[I-1+Q//3][J-1+Q%3]
  for(N,O)in[[-1,0],[1,0],[0,1],[0,-1]]:
   D,E=N*2,O*2;P=g[I+D][J+E]
   while C!=P!=A<len(g[0])>G+E>-1<F+D<len(g)>g[F+D][G+E]!=A:g[F+D][G+E]=P;D+=N;E+=O
 for Q in range(25):g[I-2+Q//5][J-2+Q%5]=A
 return g
