# zip fiddling
def p(g):
 for i in(M:={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g}):
  for I in M:
   s={I}
   for j in[*M]*3:
    if M[i]==M[I]!=any(0<abs(i-I)<2for I in M)<any(0<abs(j-I)<2for I in s):s|={j};g[int((j-I+i).imag)][int((-(-1)**M[I]*(j-I)+i).real)]=M[j]
 return g