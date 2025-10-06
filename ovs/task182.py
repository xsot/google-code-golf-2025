def p(g):
 R=F=sum(g,[])
 while C:=[*{*F}][-2]:
  o=F.index(C)-2;N={d for d in range(70)if d%20<6>F[d+o]==C}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g

## 219
p=lambda g,k=-51,h=4:k*g or p([[v*(h:=h*2)and[max(V&7for r in g if((V:=(R:=r+[869,v]*2)[R.index(869)+3])^v)<8),v|h,*[p*(p%8==v%8)|v]*49,v//(v&v%8-v or 1)%197*8+v%8][k]for p,v in zip([0]+r,r)]for*r,in zip(*g[::-1])],k+1)
