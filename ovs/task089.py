def p(g):
 for i in(M:={A*1j+x:F for A,r in enumerate(g)for x,F in enumerate(r)if F}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i]==M[I]!=any(0<abs(i-I)<2for I in M)<any(0<abs(y-I)<2for I in s):s|={y};g[int((y-I+i).imag)][int(((I-y)*(-1)**M[I]+i).real)]=M[y]
 return g
