# based on Garry Moss' solution
def p(p):
 z,t,T=[{(l,n)for l,p in enumerate(p)for n,p in enumerate(p)if p==C}for C in(0,2,5)]
 for n in 2,3:
  R=[t-t]
  for d,i in(Q:=z|t|T):v=Q&{*sum([[(d+l,i),(d,i+l)]for l in range(-n,n+1)],[])};R+=[l|v for l in R if Q-z-l>v]
  for l in R:
   if t<=l:
    for l,n in l&T:p[l][n]=8
    return p

##

def p(g,F=0):
 for W in 4,4,3:
  for i in range(h:=len(g)):
   for j in range(w:=len(g[0])):
    X=[(i+d%3*k-k,j+d%5*k-k)for k in range(W)for d in b'adeo']
    for I,J in{*X*all(V:=[not h>I>-1<J<w or g[I][J]for I,J in X])*(2in V[W%4-W:]or F)*(1<V[3:].count(2)==sum(5-v&v%~4for r in g[i-min(W,i):i-~W]for v in r[j-min(W,j):j-~W]))}:
     if h>I>-1<J<w:F=g[I][J]=2+g[I][J]%2*6
 return g
