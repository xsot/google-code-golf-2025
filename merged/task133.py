# combined (475 vs 330 bytes for gold)
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
