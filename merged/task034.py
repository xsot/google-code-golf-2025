# joking (178 vs 2500 bytes for gold)
p=lambda i,k=27:-k*i or p([[(u==2>1>s+t)*2or(s*t*y>1or 2in[s,t]*u)*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0,*x],f,[0,*f])]for*x,f in zip(*i,[[0]*9,*zip(*i)])][::-1],k-1)


##
p=lambda i,k=27:-k*i or p([[(u==2>s+t<1)*2or(y>0<s*t or u>0<2in[s,t])*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0,*x],f,[0,*f])]for*x,f in zip(*i,[[0]*9,*zip(*i)])][::-1],k-1)

### combined (181 bytes)
p=lambda i,k=27:-k*i or p([[(u==2>s+t<1)*2or(y>0<s*t or u>0<2in[s,t])*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0,*x],f,[0,*f])]for*x,f in zip(*i,[[0]*9,*zip(*i)])][::-1],k-1)

### ovs (220 bytes)
def p(g):
 f=sum(g,[]);C,={*f}-{0,2};i=min(map(f.index,(2,C)))
 for d in-1,1:
  for D in-1,0:
   o=i//9-~d//2;O=i%9-D
   for a,A in[w:=(d,0),(-d,D|1),w]*9*(g[o][O]==2):
    if-1<o<9>O>-1:g[o][O]=C
    o+=a;O-=A
 return g
