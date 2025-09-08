# ovs (236 (278 unzipped) bytes, gold)
def p(g):
 for i in(M:={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i]==M[I]!=any(0<abs(i-I)<2for I in M)<any(0<abs(y-I)<2for I in s):s|={y};g[int((y-I+i).imag)][int(((I-y)*(-1)**M[I]+i).real)]=M[y]
 return g

## 266 unzipped:

L=lambda i,s:any(0<abs(i-I)<2for I in s)
def p(g):M={A//13*1j+A%13:F for A,F in enumerate(sum(g,[]))if F};[0for i in M for I in M if(s:={I})for y in[*M]*3for g[int((y-I+i).imag)][int(((I-y)*(-1)**M[I]+i).real)]in[M[y]][:M[i]==M[I]!=L(i,M)<L(y,s)!=s.add(y)]];return g

### mwi (259 (284 unzipped) bytes)
L=lambda i,j,s:any(0<(i-I)**2+(j-J)**2<3for I,J in s)
def p(g):
 for i,j in(M:={(A,x):F for A,r in enumerate(g)for x,F in enumerate(r)if F}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i,j]==M[I]!=L(i,j,M)<L(*y,s):s|={y};g[y[0]-I[0]+i][(I[1]-y[1])*(-1)**M[I]+j]=M[y]
 return g

### combined (290 (376 unzipped) bytes)
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
