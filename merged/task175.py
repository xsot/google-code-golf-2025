# mwi (75 bytes, gold)
r=range(21);p=lambda g:[[g[A][B]|g[B][A]or g[0][B!=A]for B in r]for A in r]

### combined (92 bytes)
e=enumerate
p=lambda g:[[[C|g[B][A]or g[0][1],g[0][0]][B==A]for(B,C)in e(B)]for(A,B)in e(g)]
