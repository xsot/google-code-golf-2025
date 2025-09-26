# based on Garry Moss' solution
def p(I):
 for n in(2,3):
  t,z,T,*R=[{(l,N)for l,I in enumerate(I)for N,I in enumerate(I)if I>=n}for n in(2,0,5,7)]
  for d,i in z:v={(l,N)for l,N in z if abs(d-l+(i-N)*1j)in(2,0,1,n)};R+=[l|v for l in R if t-l>v]
  for l in R:
   if t-T<l:
    for d,i in l&T:I[d][i]=8
    return I

##

def p(g,F=0):
 for W in 4,4,3:
  for i in range(h:=len(g)):
   for j in range(w:=len(g[0])):
    X=[(i+d%3*k-k,j+d%5*k-k)for k in range(W)for d in b'adeo']
    for I,J in{*X*all(V:=[not h>I>-1<J<w or g[I][J]for I,J in X])*(2in V[W%4-W:]or F)*(1<V[3:].count(2)==sum(5-v&v%~4for r in g[i-min(W,i):i-~W]for v in r[j-min(W,j):j-~W]))}:
     if h>I>-1<J<w:F=g[I][J]=2+g[I][J]%2*6
 return g
