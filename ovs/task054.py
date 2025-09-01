def p(g):
 f=sum(g,[]);*C,_,B=sorted({*f},key=f.count);M={(i,j):v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={(i,j)for i,j in M for I,J in M if(I-i)**2+(J-j)**2==1}
 for i,j in{*M}-T:
  for I,J in T:
   y,x=zip(*T);d=I-sum(y)//len(y);D=J-sum(x)//len(x);g[I][J]=B;F=1
   while((r:=g[d+i])[D+j]^B)*F:r[D+j]=M[I,J];d+=(d>0)-(d<0);D+=(D>0)-(D<0);F-=-3<d|D<3
 return g
