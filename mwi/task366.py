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