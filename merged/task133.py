# ovs (300 (389 unzipped) vs 330 bytes for gold)
def p(g):
 *C,M={i*90+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g},
 for A in M:
  G={A}
  for D in*C,:
   if{A-90,A-1}&D:C.remove(D);G|=D
  C+=G,
 for A in C:
  for D in A:
   for G in A:
    for I in 1//sum(M[k]==M[D]for k in A)*C:
     for Q in{G}^A:
      for V in(E:=[k for k in I if M[D]==M[k]==M[G]]):V+=(len(E)^6)%6*(Q-G);g[V//90][V%90],={*map(M.get,I)}-{M[D]}
 return g

## worse for compression, 312/378:

def p(g):
 e,*C=enumerate,;M={i*90+j:v for i,r in e(g)for j,v in e(r)if v}
 for A in M:
  G={A}
  for D in*C,:
   if{A-90,A-1}&D:C.remove(D);G|=D
  C+=G,
 [0for A in C for D in A for G in A for I in 1//sum(M[k]==M[D]for k in A)*C for Q in{G}^A if(E:=[k for k in I if M[D]==M[k]==M[G]])for V in E for W in[V+(len(E)^6)%6*(Q-G)]for g[W//90][W%90]in{*map(M.get,I)}-{M[D]}];return g

### combined (330 (475 unzipped) bytes)
def p(g):
 C=[];e=enumerate
 for A,r in e(g):
  for B,F in e(r):
   G={(A,B)}
   for D in(F>0)*C:
    if{(A-1,B),(A,B-1)}&D:C.remove(D);G|=D
   C+=(F>0)*[G]
 for A in C:
  B=[g[A][B]for(A,B)in A];D=min({*B},key=B.count);G,H=max([A,B]for(A,B)in A if g[A][B]==D)
  for I in 1//B.count(D)*C:
   for(Q,R)in A-{(G,H)}:
    for J,_ in e(E:=[[A,B]for(A,B)in I if g[A][B]==D]):F=(len(E)^6)%6;O,P=min(E);g[O+(Q-G)*F+J//F][P+(R-H)*F+J%F]=max(g[A][B]for(A,B)in I if g[A][B]^D)
 return g
