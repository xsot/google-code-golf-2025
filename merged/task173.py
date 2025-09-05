# ovs (228 (271 unzipped) vs 2500 bytes for gold)
def p(g):o=[(Y,x,y)for Y,a in enumerate(g)for x,a in enumerate(a)if(y:=[a for a in g[Y:Y+3]for a in a[x:x+3]])==y[::-1]>y[:8]>[0]*8];[0for Y,X,a in o for Y,X,A in o for y,g[Y+y//3][X+y%3]in enumerate(a*(len({*a})==3*len({a[y]for y,r in enumerate(A)if r-a[y]})))];return g

## very close to not need compression, 241/245:
def p(g):e=enumerate;o=[(y,x,s)for y,r in e(g)for x,c in e(r)if(s:=sum([r[x:x+3]for r in g[y:y+3]],[]))==s[::-1]>s[:8]>[0]*8];[0for*_,a in o for Y,X,A in o for y,g[Y+y//3][X+y%3]in e(a*(len({*a})==3*len({y for y,r in zip(a,A)if y^r})))];return g

### combined (247 (277 unzipped) bytes)
def p(g):
 e=enumerate;o=[(s,y,x)for y,r in e(g)for x,c in e(r)if any(s:=sum([r[x:x+3]for r in g[y:y+3]],[]))*s==s[::-1]and s[8:]]
 for a,y,x in o:
  for A,Y,X in o:
   for y,r in e(a*(len({*a})==3*any(all(a[y]in[r,V]for y,r in e(A))for V in{*a}))):g[Y+y//3][X+y%3]=r
 return g
