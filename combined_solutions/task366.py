def p(g):
 L=enumerate;M=sum(g,[]);*S,J,K,E=sorted({*M},key=M.count);F=[]
 if(Q:={K,E}<={*g[0]}):g=[*map(list,zip(*g))]
 for(A,f)in L(g):
  for(B,N)in L(f):
   if E!=N!=K in f:
    C={(A,B)}
    for D in[*F]:
     if{(A-1,B),(A,B-1)}&D:F.remove(D);C|=D
    F+=[C]
 for D in sorted(F,key=lambda s:-sum(g[A][B]!=J for(A,B)in s)):
  G,H=min(D)
  for(A,f)in L(g):
   for(B,N)in L(f):
    if E in f and all(len(g[0])>B+N-H>-1<A+f-G<len(g)and(J!=g[f][N]==g[f+A-G][N+B-H]!=E or J==g[f][N]and g[f+A-G][N+B-H]==E)for(f,N)in D):
     for(O,P)in D:g[A+O-G][B+P-H]=g[O][P]
 g=[A for A in g if E in A];return[g,[*zip(*g)]][Q]