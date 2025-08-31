# combined (426 (612 unzipped) vs 374 bytes for gold)
def p(g):
 L=enumerate;M=sum(g,[]);*S,J,K,E=sorted({*M},key=M.count);F=[]
 if(Q:={K,E}<={*g[0]}):g=[*map(list,zip(*g))]
 for A,f in L(g):
  for B,N in L(f):
   if E!=N!=K in f:
    C={(A,B)}
    for D in[*F]:
     if{(A-1,B),(A,B-1)}&D:F.remove(D);C|=D
    F+=[C]
 for D in sorted(F,key=lambda s:-sum(g[A][B]!=J for(A,B)in s)):
  G,H=min(D)
  for(I,A)in L(g):
   for(C,B)in L(A):
    if E in A and all(len(g[0])>C+B-H>-1<I+A-G<len(g)and(J!=g[A][B]==g[A+I-G][B+C-H]!=E or J==g[A][B]and g[A+I-G][B+C-H]==E)for(A,B)in D):
     for(O,P)in D:g[I+O-G][C+P-H]=g[O][P]
 g=[A for A in g if E in A];return[g,[*zip(*g)]][Q]

### xsot (612 bytes)
# combined (426 (612 unzipped) vs 374 bytes for gold)
def p(g):
 L=enumerate;M=sum(g,[]);*S,J,K,E=sorted({*M},key=M.count);F=[]
 if(Q:={K,E}<={*g[0]}):g=[*map(list,zip(*g))]
 for A,f in L(g):
  for B,N in L(f):
   if E!=N!=K in f:
    C={(A,B)}
    for D in[*F]:
     if{(A-1,B),(A,B-1)}&D:F.remove(D);C|=D
    F+=[C]
 for D in sorted(F,key=lambda s:-sum(g[A][B]!=J for(A,B)in s)):
  G,H=min(D)
  for(I,f)in L(g):
   for(C,B)in L(f):
    if E in f and all(len(g[0])>C+B-H>-1<I+f-G<len(g)and(J!=g[f][B]==g[f+I-G][B+C-H]!=E or J==g[f][B]and g[f+I-G][B+C-H]==E)for(f,B)in D):
     for(O,P)in D:g[I+O-G][C+P-H]=g[O][P]
 g=[A for A in g if E in A];return[g,[*zip(*g)]][Q]
