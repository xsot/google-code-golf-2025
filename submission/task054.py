def p(g):
 f=sum(g,[]);*C,_,B=sorted({*f},key=f.count);M={(i,j):v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={(i,j)for i,j in M for I,J in M if(I-i)**2+(J-j)**2==1}
 for i,j in{*M}-T:
  for I,J in T:
   y,x=zip(*T);d=I-sum(y)//len(y);D=J-sum(x)//len(x);g[I][J]=B;F=1;u=d+i;U=D+j
   while(g[u][U]^B)*F:g[u][U]=M[I,J];u+=int(d/2);U+=int(D/2);F-=-2<d|D<2
 return g