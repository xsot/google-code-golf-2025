def p(g):
 *C,M={A*66+j:(g)for A,g in enumerate(g)for j,g in enumerate(g)if g},
 for A in M:G={A};C=[D for D in C if D==D-{A-66,A-1}or G.update(D)]+[G]
 for D in C:
  for A in D:
   for G in D:
    I=D
    for I in 1//len([V for V in I if M[A]==M[V]])*C:
     for Q in D-{G}:
      for V in[V for V in I if M[A]==M[V]==M[G]]:V+=(len([V for V in I if M[A]==M[V]==M[G]])^6)%6*(Q-G);g[V//66][V%66],={M[V]for V in I}-{M[A]}
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
