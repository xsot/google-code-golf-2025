# optimized for pre-zip length
def p(g):
 e,R,G=enumerate,range,g[-5:]
 for s in[()]*4:G=[x for x in zip(*G[::-1])if{*x}-{0,4}];g=[[*x]for x in zip(*g[::-1])if 4in(s:=s+x)]
 for x in R(1200):
  s,y=x//400+2,x%400//20;x%=20;H,W=len(G)*s,len(G[0])*s
  if all(c in[0,4-4*(y<=Y<y+H>0<x<=X<x+W)or G[(Y-y)//s][(X-x)//s]]for Y,r in e(g)for X,c in e(r)):
   for Y in R(H*W):X=Y%W;Y//=W;g[Y+y][X+x]=G[Y//s][X//s]
   return g