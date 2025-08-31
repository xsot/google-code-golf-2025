def p(m):
 E=enumerate;a=sum(m,A:=[]);*_,B,S,D=sorted({*a},key=a.count)
 if{S,D}<={*m[0]}:return[*zip(*p([*map(list,zip(*m))]))]
 for(y,r)in E(m):
  for(x,v)in E(r):
   if D!=v!=S in r:c={(y,x)};[A.remove(d)or(c:=c|d)for d in[*A]if{(y-1,x),(y,x-1)}&d];A+=c,
 for C in sorted(A,key=lambda s:-sum(B!=m[y][x]for(y,x)in s)):
  G,H=min(C)
  for(y,r)in E(m):
   for(x,v)in E(r):
    for(O,P)in[*C]*all(len(m[0])>c+(w:=x-H)>-1<r+(h:=y-G)<len(m)and(B!=m[r][c]==m[r+h][c+w]or B==m[r][c]and m[r+h][c+w]==D)for(r,c)in C):m[O+h][P+w]=m[O][P]
 return[r for r in m if D in r]