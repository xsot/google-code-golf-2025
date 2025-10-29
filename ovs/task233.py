def p(g):
 for G in 92*[g]:g=[[*G]for G in zip(*g[('2, '*4in str(g[-1]))-2::-1])]
 for G in 92*[[G[x:3+x]for G in G[y:3+y]]for y,p in enumerate(G[2:])for x,p in enumerate(p[2:])][::-1]:
  for y,p in enumerate(g*({*sum(G,[])}^{0}>{2,0})):
   for x,p in enumerate(p):
    for n,p in enumerate(G*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in enumerate(G)for m,p in enumerate(p))):g[n+y][x:3+x],*G=p,
  G[:]=[[*G]for G in zip(*G[::-1])]
 return g
# 44 would work instead of 92, but apparently it compresses worse

##
e=enumerate
def p(g):
 for G in[g]*60:*g,=map(list,zip(*g[max(map(len,str(g[0]).split('0')))<12:][::-1]))
 for s in [[v[x:x+3]for v in G[y:y+3]]for y,p in e(G[2:])for x,p in e(p[2:])][::-1]*4:
  for y,p in e(g*({*sum(s,s[0])}^{0}>{2,0})):
   for x,p in e(p):
    for n,p in e(s*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in e(s)for m,p in e(p))):g[n+y][x:x+3],*s=p,
  s[:]=zip(*s[::-1])
 return g
