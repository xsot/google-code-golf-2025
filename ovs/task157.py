def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(16+t%15-w):
  for s in 0,1:
   u=*map(list,g),
   for x in u[6:]:
    s+=any(x[t:w])
    for b in range(w-t):u[s][b+l]+=x[b+t]>4;x[b+t]=0
   g=p(u)or g
 if{*sum(g[:3],[])}=={1,2}:return g

##

def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   A in p or 0in(x-y-4%y<=min(x-y for x,y in zip(A,c))for x,y in zip(A,c))or Q(o+len(A),p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*len(A)):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(b'\n%0s\n'%A)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=b'\n%0s\n'%bytes(K);S={*K.split(b'\n')};Q(0,{});return g
# the 0 in %0s is necessary to avoid variable substitution replacing the s with another letter
