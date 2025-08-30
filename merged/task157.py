# combined (391 vs 296 bytes for gold)
t=b'\n'
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   h=len(A);A in p or h==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+h,p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*h):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(t+A+t)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=t+bytes(K)+t;S={*K.split(t)};Q(0,{});return g

### ovs (tied, 391 bytes)
t=b'\n'
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   h=len(A);A in p or h==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+h,p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*h):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(t+A+t)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=t+bytes(K)+t;S={*K.split(t)};Q(0,{});return g
