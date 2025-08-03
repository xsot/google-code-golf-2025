def p(m):
 N,M=len(m),len(m[0]);z=0,
 for i in range(N*M):
  b=m[y:=i%N][x:=i//N];w=h=1
  while x+w<M>0<m[y][x+w]==b:w+=1
  while y+h<N>0<m[y+h][x]==b:h+=1;z=max(z,(w*h,b))
 return[[z[1]]*2]*2

###
def p(m):
 N,M=len(m),len(m[0]);z=0,
 for i in range(N*M):
  Y=y=i%N;X=x=i//N;b=m[y][x]
  while-~X<M>0<m[y][X+1]==b:X+=1
  while-~Y<N>0<m[Y+1][x]==b:Y+=1;z=max(z,((Y-y+1)*(X-x+1),b))
 return[[z[1]]*2]*2