def p(g):
 for G in 92*[g]:g=[[*G]for G in zip(*g[all(G==G[:12]for G in str(g[0]).split('0')):][::-1])]
 for G in 92*[[G[x:3+x]for G in G[y:3+y]]for y,p in enumerate(G[2:])for x,p in enumerate(p[2:])][::-1]:
  for y,p in enumerate(g*({*sum(G,[])}^{0}>{2,0})):
   for x,p in enumerate(p):
    for n,p in enumerate(G*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in enumerate(G)for m,p in enumerate(p))):g[n+y][x:3+x],*G=p,
  G[:]=[[*G]for G in zip(*G[::-1])]
 return g

##
def p(g):
 for G in #[*range(60,100,4)]##*[g]:g=[[*G]#['','[::-1]']##for G in zip(*g[all(G==G[:12]for G in str(g[0]).split('0')):]#[*{'','[::-1]'*('[::-1]'not in prev_vals[-1:])}]##)]#['[::-1]'*('[::-1]'not in prev_vals[-2:])]##
 for G in #[prev_vals[0]]##*[[G[x:3+x]for G in G[y:3+y]]for y,p in enumerate(G[2:])for x,p in enumerate(p[2:])][::-1]:
  for y,p in enumerate(g*({*sum(G,[])}^{0}>{2,0})):
   for x,p in enumerate(p):
    for n,p in enumerate(G*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in enumerate(G)for m,p in enumerate(p))):g[n+y][x:3+x],*G=p,
  G[:]=[[*G]#['','[::-1]']##for G in zip(*G#['[::-1]'*('[::-1]'!=prev_vals[-1])]##)]
 return g