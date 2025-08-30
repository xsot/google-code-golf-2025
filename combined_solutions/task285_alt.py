# Shorter before zlib
def p(g,e=enumerate):
 G=eval(str(g))
 for y,r in e(g[:-1]):
  for x,c in e(r[:-1]):
   if len({c,r[x+1],g[y+1][x],g[y+1][x+1]})>3:
    for Y in(v:=range(5-(151==y*x+c))):
     for X in v:
      if max(d:=[((G[H][W]==G[y+h][x+w])*any((G[y+h+i][x+w+j],G[y+h][x+w+j],G[y+h+i][x+w])),G[H][W],H,W,G[y+h][x+w])for h,w in((0,1),(1,0),(1,1),(0,0))if-1<(W:=x+(j:=2*w-1)*X+w)<len(g)>(H:=y+(i:=2*h-1)*Y+h)>-1])[0]:
       for a,b,H,W,q in d:g[H][W]=q
 return g