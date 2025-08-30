# ovs (220 vs 160 bytes for gold)
def p(g):
 f=sum(g,[]);C,={*f}-{0,2};i=min(map(f.index,(2,C)))
 for d in-1,1:
  for D in-1,0:
   o=i//9-~d//2;O=i%9-D
   for a,A in[w:=(d,0),(-d,D|1),w]*9*(g[o][O]==2):
    if-1<o<9>O>-1:g[o][O]=C
    o+=a;O-=A
 return g
