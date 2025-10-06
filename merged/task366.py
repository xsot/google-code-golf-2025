# joking (302 (495 unzipped) bytes, gold)
def p(g):
 *s,m,b,B=sorted({*sum(g,[])},key=sum(g,[]).count)
 *s,=g,
 for r in s*6:
  for r in s+(s:=[]):
   s+=[],
   for r in zip(*r):s+=s.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 [6for y,s in sorted((-sum(m^s for s in s for s in s),s)for s in s)for y,r in enumerate(g)for x,r in enumerate(r)for h,r in zip(g[y:]+g,s*all((a==r)!=(m==r)==(a==B)for h,r in zip(g[y:]+g,s)for a,r in zip(h[x:x+len(r)]+g,r)))for h[x:x+len(r)]in[r]];return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]

##
def p(g):
 *s,m,b,B=sorted({*sum(g,[])},key=sum(g,[]).count)
 *s,=g,
 for r in s*#[6,8]##:
  for r in s+(s:=[]):
   s+=[],
   for r in zip(*r):s+=s.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 [#[*range(10)]##for #[*'yrsx']##,s in sorted((-sum(m^s for s in s for s in s),s)for s in s)for y,r in enumerate(g)for x,r in enumerate(r)for h,r in zip(g[y:]+g,s*all((a==r)!=(m==r)==(a==B)for h,r in zip(g[y:]+g,s)for a,r in zip(h[x:x+len(r)]+g,r)))for h[x:x+len(r)]in[r]]#[';','\n ']##return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]

### mwi (310 (493 unzipped) bytes)
# zip-optimized version of ovs's
def p(g):
 r,*s=sum(g,[]),g;*r,m,b,B=sorted({*r},key=r.count)
 for t in s*6:
  for t in s+(s:=[]):
   s+=[],
   for r in zip(*t):s+=s.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 for r,s in sorted((-sum(m^s for s in s for s in s),s)for s in s):
  for y,r in enumerate(g):
   for x,r in enumerate(r):
    for h,r in zip(g[y:],all((a!=r)==(r==m)==(B==a)for h,r in zip(g[y:]+g,s)for a,r in zip(h[x:x+len(r)]+g,r))*s):h[x:x+len(r)]=r
 return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]

##
def p(m):
 *H,B,S,D=sorted({*sum(m,C:=[])},key=sum(m,C:=[]).count)
 for y,r in enumerate(m):
  for x,v in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
 for y,(G,H),(g,h),*C in sorted((-sum(B!=m[r][c]for r,c in C),min(C),max(C),*C)for C in C):
  for y,r in enumerate(m[:G-g]):
   for x,v in enumerate(r[:H-h]):
    for r,c in C*all(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c]for r,c in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for r in zip(*[r for r in zip(*m)if D in r])if D in r]

## alternate approach that extracts shapes instead of getting their coords
def p(g):
 f,z=sum(g,[]),[g];*_,m,b,B=sorted({*f},key=f.count)
 for _ in z*6:
  for t in z+(z:=[]):
   z+=[[]]
   for r in zip(*t):z+=[z.pop()+[r]if({*r}-{b}and{*r}-{B}=={*r})or{*r}>{b}else[]]
 for _,s in sorted((-sum(x!=m for x in sum(s,(0,))),s)for s in z if s):
  for y,r in enumerate(g[:1-len(s)]):
   for x,c in enumerate(r[:1-len(s[0])]):
    G=[r[:]for r in g];k=1
    for h,R in enumerate(s):k&=all(B!=g==r!=m or g==B!=r==m for g,r in zip(G[y+h][x:x+len(R)],R));G[y+h][x:x+len(R)]=R
    if k:g=G
 return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]

### ovs (317 (493 unzipped) bytes)
# based on mwi's alternate approach
def p(g):
 r,*z=sum(g,[]),g;*_,m,b,B=sorted({*r},key=r.count)
 for _ in z*6:
  for t in z+(z:=[]):
   z+=[],
   for r in zip(*t):z+=z.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 for _,s in sorted((-sum(x^m for t in s for x in t),s)for s in z):
  for y,r in enumerate(g):
   for x,r in enumerate(r):
    for h,r in zip(g[y:],all((a!=r)==(r==m)==(B==a)for h,r in zip(g[y:]+g,s)for a,r in zip(h[x:x+len(r)]+g,r))*s):h[x:x+len(r)]=r
 return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]

## 455 without compression:

E=enumerate;S=sorted;Z=zip
def p(g):
 f,*z=sum(g,[]),g;*_,m,b,B=S({*f},key=f.count)
 for _ in z*6:
  for t in z+(z:=[]):
   z+=[],
   for r in Z(*t):z+=z.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 [0for s in S(z,key=lambda s:-sum(x^m for x in sum(s,())))for y,r in E(g)for x,_ in E(r)for h,h[x:x+len(s[0])]in Z(g[y:],all([a==r!=m,r==m][B==a]for h,R in Z(g[y:]+g,s)for a,r in Z(h[x:x+len(R)]+g,R))*s)];[g:=[r for r in Z(*g)if B in r]for _ in'  '];return g

### xsot (364 (613 unzipped) bytes)
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

### garry_moss (371 (651 unzipped) bytes)
def p(r):g=len(r)>len(r[0]);n=[*map(list,(r,zip(*r))[g])];f,o=len(n),len(n[0])>>1;i,r=sorted([[r[:o]for r in n],[r[o:]for r in n]],key=lambda r:len(set(sum(r,[]))));y,a=sorted(set(p:=sum(r,[])),key=p.count)[-2:];u=max(set(p:=sum(i,[])),key=p.count);[exec('for r in r[t:t+e]:r[n:n+s]=[a]*s')or[all(i[t+a][n:n+s]==[(a,u)[a==y]for a in k[a]]for a in range(e))and exec('for a in range(e):i[t+a][n:n+s]=k[a]')for t in range(f-e+1)for n in range(o-s+1)]for g in range(3,0,-1)for t in range(f)for n in range(o)for e in range(f-t,0,-1)for s in range(o-n,0,-1)if a not in(p:=sum(k:=[r[n:n+s]for r in r[t:t+e]],[]))and e*s-p.count(y)==g];return(i,[*zip(*i)])[g]

### combined (406 (561 unzipped) bytes)
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
