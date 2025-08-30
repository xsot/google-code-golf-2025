def p(g):
 R=range;t=sum(g,[]);*v,B=sorted({*t},key=t.count)
 for u in v:
  G=[[[B,u][c==u]for*l,c in zip(*g,r)if u in l]for r in g if u in r]
  for y in R(-9,len(g)):
   for x in R(-9,len(g[0])):
    q=eval(str(g));W=T=-1
    for Y in R(len(G)*2):
     for X in R(len(G[0])*2):
      if len(g[0])>X+x>-1<Y+y<len(g):
       if T<0<G[Y//2][X//2]^B:T=q[y+Y][x+X]
       W&=T<0 or(q[y+Y][x+X]==T)==(G[Y//2][X//2]==u);q[y+Y][x+X]=G[Y//2][X//2]
    if({*str(q)}<{*str(g)})*W>0:return G