def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for i in range(N*M):
  Y=y=i%N;X=x=i//N
  while(m[y]*2)[X]==b<M>X:X+=1
  while Y<N!=(m[Y]*2)[x]==b:Y+=1;z=max(z,[sum(sum(a:=[[d*(e>0)for e in l[x:X]]for l in m[y:Y]],[]))//d,a])
 return z[1]