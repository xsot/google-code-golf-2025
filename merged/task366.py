# mwi (365 (604 unzipped) bytes, gold)
def p(m):
 *H,B,S,D=sorted({*sum(m,C:=[])},key=sum(m,C:=[]).count)
 if{*m[0]}>={S,D}:return[*zip(*p([[*C]for C in zip(*m)]))]
 for y,r in enumerate(m):
  for x,v in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
 for y,(G,H),*C in sorted((-sum(B!=m[r][c]for r,c in C),min(C),*C)for C in C):
  for y,r in enumerate(m):
   for x,v in enumerate(r):
    for r,c in C*all(len(m[0])>x-H+c>-1<y-G+r<len(m)and(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c])for r,c in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for y,r in enumerate(m)if D in r]

### xsot (366 (613 unzipped) bytes)
def p(m):
 *_,B,S,D=sorted({*sum(m,C:=[])},key=sum(m,C:=[]).count)
 if(S in m[0])*(D in m[0]):return[*zip(*p([[*C]for C in zip(*m)]))]
 for y,r in enumerate(m):
  for x,v in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
 for y,(G,H),*C in sorted((-sum(B!=m[r][c]for r,c in C),min(C),*C)for C in C):
  for y,r in enumerate(m):
   for x,v in enumerate(r):
    for r,c in C*all(len(m[0])>x-H+c>-1<y-G+r<len(m)and(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c])for r,c in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for y,r in enumerate(m)if D in r]

##
def p(m):
 a=sum(m,C:=[]);*_,B,S,D=sorted({*a},key=a.count)
 if(S in m[0])*(D in m[0]):return[*zip(*p([*map(list,zip(*m))]))]
 for(y,r)in enumerate(m):
  for(x,v)in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
# greedily start with the shape with the most dots
 for(y,(G,H),*C)in sorted((-sum(B!=m[r][c]for(r,c)in C),min(C),*C)for(C)in C):
  for(y,r)in enumerate(m):
   for(x,v)in enumerate(r):
# try to place this shape here: dots must match, and if one side has a dot the other must too
    for(r,c)in C*all(len(m[0])>x-H+c>-1<y-G+r<len(m)and(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c])for(r,c)in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for(y,r)in enumerate(m)if D in r]

### combined (411 (561 unzipped) bytes)
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
