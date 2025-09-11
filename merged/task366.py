# mwi (364 (604 unzipped) vs 365 bytes for gold)
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

### xsot (365 (613 unzipped) bytes)
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

### garry_moss (372 (651 unzipped) bytes)
def p(r):g=len(r)>len(r[0]);n=[*map(list,(r,zip(*r))[g])];f,o=len(n),len(n[0])>>1;i,r=sorted([[r[:o]for r in n],[r[o:]for r in n]],key=lambda r:len(set(sum(r,[]))));y,a=sorted(set(p:=sum(r,[])),key=p.count)[-2:];u=max(set(p:=sum(i,[])),key=p.count);[exec('for r in r[t:t+e]:r[n:n+s]=[a]*s')or[all(i[t+a][n:n+s]==[(a,u)[a==y]for a in k[a]]for a in range(e))and exec('for a in range(e):i[t+a][n:n+s]=k[a]')for t in range(f-e+1)for n in range(o-s+1)]for g in range(3,0,-1)for t in range(f)for n in range(o)for e in range(f-t,0,-1)for s in range(o-n,0,-1)if a not in(p:=sum(k:=[r[n:n+s]for r in r[t:t+e]],[]))and e*s-p.count(y)==g];return(i,[*zip(*i)])[g]

### combined (407 (561 unzipped) bytes)
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
