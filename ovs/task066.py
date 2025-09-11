def p(g):
 M={A*1j+B:D for A,C in enumerate(g)for B,D in enumerate(C)};A,C=[y for y in M if M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
 for*V,y,A,C,G in S:
  if(y in M)*16>G|C+13:
   for y in(M[y]==2)*V:g[int(y.imag)][int(y.real)]=3
   F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for D in[A][F:]or[A*1j,A/1j]*G]
 return g
