L=lambda i,j,s:any(0<(i-I)**2+(j-J)**2<3for I,J in s)
def p(g):
 for i,j in(M:={(A,x):F for A,r in enumerate(g)for x,F in enumerate(r)if F}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i,j]==M[I]!=L(i,j,M)<L(*y,s):s|={y};g[y[0]-I[0]+i][(I[1]-y[1])*(-1)**M[I]+j]=M[y]
 return g