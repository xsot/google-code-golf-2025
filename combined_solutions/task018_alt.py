def p(g):
 C=[];e=enumerate
 for A,r in e(g):
  for B,F in e(r):
   G={(A,B)}
   for D in(F>0)*C:
    if{(A-1,B),(A,B-1)}&D:C.remove(D);G|=D
   C+=(F>0)*[G]
 u=sum(g,[]);G=max({*u}-{0},key=u.count)
 for D in[[A,{(A,B,g[A][B])for(A,B)in A if g[A][B]^G}]for A in C if any(G==g[A][B]for(A,B)in A)]:
  H=1
  for(A,B)in D[0]:g[A][B]=0
  for L in'for'*4:
   g=[[[*A][::-1]for A in zip(*g)],g[::-1]][L>'f']
   for E in(C:=range(-20,20)):
    for F in C:
     if H*all(len(g[0])>B+F>-1<A+E<len(g)>C==g[A+E][B+F]for(A,B,C)in D[1]):
      for(A,B)in D[0]:g[A+E][B+F]=G
      for(A,B,K)in D[1]:g[A+E][B+F]=K;H=0
 return g