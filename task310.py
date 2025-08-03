def p(m):
 b=min(set(a:=sum(m,[])),key=a.count);N=len(m)
 for i in range(N*N):
  Y=y=i%N;X=x=i//N
  if m[y][x]==b:
   while-~X<N!=m[y][X+1]==b:X+=1
   while-~Y<N!=m[Y+1][x]==b:Y+=1
   return[l[x:X+1]for l in m[y:Y+1]]