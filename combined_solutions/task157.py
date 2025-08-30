def p(g):
 E=enumerate;z=[]
 for r,R in E(g):
  for c,e in E(R):
   x={(r,c)}
   for s in[*z]*(e>4):
    if{(r-1,c),(r,c-1)}&s:z.remove(s);x|=s
   z+=[x]*(e>4)
 for r,R in E(g[:3]):
  for c,e in E(R):
   for s in[*z]:
    Y,X=min(s);G=eval(str(g))
    if all(w-X+c<15>g[h-Y+r][w-X+c]<1for h,w in s):
     for h,w in s:G[h-Y+r][w-X+c]=1;G[h][w]=0
     if("2, 0, 1"in str([*zip(*G[:3])]))+("1, 0"in str(G[:3]+G[:3][::-1]))<1:z.remove(s);g=G
 return g