def p(m):
 a=sum(m,C:=[]);*_,B,S,D=sorted({*a},key=a.count)
 if(S in m[0])*(D in m[0]):return[*zip(*p([*map(list,zip(*m))]))]
 for(y,r)in enumerate(m):
  for(x,v)in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
 for(y,(G,H),*C)in sorted((-sum(B!=m[r][c]for(r,c)in C),min(C),*C)for(C)in C):
  for(y,r)in enumerate(m):
   for(x,v)in enumerate(r):
    for(r,c)in C*all(len(m[0])>x-H+c>-1<y-G+r<len(m)and(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c])for(r,c)in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for(y,r)in enumerate(m)if D in r]