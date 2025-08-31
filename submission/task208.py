def p(g):
 e=enumerate;A=g
 for G in'  ':A=[[*A]for A in zip(*A)if min(k:=sum(g,[]),key=k.count)in A];D,E=len(A),len(A[0])
 for B,r in e(g):
  for C,c in e(r[:-E]):
   if c!=A[0][0]!=sum(sum(A[C+1:C+E-1])for A in g[B+1:B+D-1])<1:return g[:B]+[f[:C]+F+f[C+E:]for F,f in zip(A,g[B:])]+g[B+D:]