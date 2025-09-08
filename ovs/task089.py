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
