# xsot (307 (465 unzipped) vs 324 bytes for gold)
e=enumerate
def p(g):
 w=[(y,x,s)for y,p in e(g[:-2])for x,p in e(p[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0,
 u=[[y[0]for y in zip(x,*g)if sum(y)]for x in g if sum(x)]
 for y,x,s in w[::-1]:
  for n,p in e(s*4):
   for y,p in e(u):
    for x,p in e(p):
     for n,p in e(s*all((2*(2*u)[n+y])[m+x]==2*(2!=r)for n,p in e(s)for m,r in e(p))):u[n+y][x:x+3]=p;s=[]
   s=*zip(*s[::-1]),
 return u

### mwi (328 (460 unzipped) bytes)
def p(g):
 e=enumerate;w=[(y,x,s)for y,r in e(g[:-2])for x,c in e(r[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0;u=[[y[0]for y in zip(x,*g)if any(y)]for x in g if any(x)]
 for y,x,s in w[::-1]:
  for p in'p in':
   for Y,R in e(u):
    for X,p in e(R):
     for n,j in e(s*all(((u*2)[n+Y]*2)[m+X]==2*(2!=r)for n,j in e(s)for m,r in e(j))):u[n+Y][X:X+3]=j;s=[]
   s=*zip(*s[::-1]),
 return u

### combined (329 (460 unzipped) bytes)
def p(g):
 e=enumerate;w=[(y,x,s)for y,r in e(g[:-2])for x,c in e(r[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,_ in e(s):g[y+n][x:x+3]=0,0,0;u=[[y[0]for y in zip(x,*g)if any(y)]for x in g if any(x)]
 for y,x,s in w[::-1]:
  for _ in'_ in':
   for Y,R in e(u):
    for X,_ in e(R):
     for n,j in e(s*all(((u*2)[n+Y]*2)[m+X]==2*(2!=r)for n,j in e(s)for m,r in e(j))):u[n+Y][X:X+3]=j;s=[]
   s=*zip(*s[::-1]),
 return u

### ovs (413 (552 unzipped) bytes)
E=enumerate
W=range
J=1j
def p(g,*S):
 V={*S};G={i*J+j:v for i,r in E(g)for j,v in E(r)}
 for I in G:
  s={I}
  for _ in' '*25:s={n for I in s for n in G if G[n]if abs(I-n)<2}-V
  if s:V|=s;S+=s,
 T,*f=sorted(S,key=lambda c:-sum(G[i]==2for i in c));(y,x),*_,(Y,X)=sorted([int(c.imag),int(c.real)]for c in T)
 for H in f:
  for a in W(4):
   o,*_=h={I*J**a:G[I]for I in H}
   for d in G:
    for I in[*h]*all((x<=(i:=I-o+d).real<=X)*(y<=i.imag<=Y)and(h[I]==2)^(G[i]>0)for I in h):G[I-o+d]=h[I]
 return[[G.get(i*J+j,0)for j in W(x,X+1)]for i in W(y,Y+1)]
