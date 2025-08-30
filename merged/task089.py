# combined (376 vs 289 bytes for gold)
def p(g):
 B=[];e=enumerate
 for A,r in e(g):
  for x,F in e(r):
   if F:
    G=[F,{(A,x)}]
    for D in[*B]:
     if{(A-1,x),(A,x-1),(A-1,x-1),(A-1,x+1)}&D[1]:B.remove(D);G[1]|=D[1]
    B+=[G]
 for x,F in B:
  for A,r in B:
   if len(r)>1==len(F)*len((H:=[D for D in r if g[D[0]][D[1]]==x])):
    for D,E in r:I,J=H[0];K,L=max(F);g[D+K-I][L+(E-J)*(x%2*2-1)]=g[D][E]
 return g
