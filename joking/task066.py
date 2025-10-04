def p(g):
 M={A*1j+C:g for A,g in enumerate(g)for C,g in enumerate(g)};A,C=[y for y in M if M[y]==3]
 for*V,y,A,G in(S:=[(A,C-A,1),(A,A-C,1)]):
  if(y in M)*G%8:
   if M[y]==2:
    for D in V:g[int(D.imag)][int(D.real)]=3
    return g
   S+=[(y-M[y]//8*A,*V,y-M[y]//8*A+D,D,~M[y]//8*G)for D in M[y]//8*[A/1j,A*1j]or[A]]