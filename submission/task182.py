def p(g):
 R=F=sum(g,[])
 while C:=max(F):
  o=F.index(C)-2;N={d for d in range(65)if d%20<6!=F[d+o:]>=[C]}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g