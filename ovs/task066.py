def p(g):
 M={D+y*1j:g for y,g in enumerate(g)for D,g in enumerate(g)};A,C=[y for y in M if M[y]==3]
 S=[(A,C-A,1),(A,A-C,1)]
 for*V,y,A,C in S:
  if(y in M)*C%8:
   if M[y]==2:return[[g|(D+y*1jin V)*3for D,g in enumerate(g)]for y,g in enumerate(g)]
   t=M[y]//8;S+={(*V,y-t*A,y-t*A+A*1j**D,A*1j**D,~t*C)for D in(t,-t)}

##
def p(g):
 M={A*1j+B:D for A,C in enumerate(g)for B,D in enumerate(C)};A,C=[y for y in M if M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
 for*V,y,A,C,G in S:
  if(y in M)*16>G|C+13:
   for y in(M[y]==2)*V:g[int(y.imag)][int(y.real)]=3
   F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for D in[A][F:]or[A*1j,A/1j]*G]
 return g
