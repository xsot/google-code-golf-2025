def p(g):
 f=sum(g,[]);*C,_,B=sorted({*f},key=f.count);M={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={i for i in M for I in M if abs(I-i)==1}
 for i in{*M}-T:
  for I in T:
   d=I-sum(T)/len(T);g[int(I.imag)][int(I.real)]=B;F=1;u=d+i
   while(g[int(u.imag)][int(u.real)]^B)*F:g[int(u.imag)][int(u.real)]=M[I];u+=d/2;F-=abs(d)<2
 return g
