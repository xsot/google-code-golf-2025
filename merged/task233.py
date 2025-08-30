# ovs (552 vs 331 bytes for gold)
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
