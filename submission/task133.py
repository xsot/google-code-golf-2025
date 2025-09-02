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