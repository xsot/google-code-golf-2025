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

## 332/501 with regex
import re
def p(g):
 *s,m,b,B=sorted({*sum(g,[])},key=sum(g,[]).count)
 *s,=g,
 for r in s*6:
  for r in s+(s:=[]):
   s+=[],
   for r in zip(*r):s+=s.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 for r,s in sorted((-sum(m^s for s in s for s in s),s)for s in s):i=-1;g=eval(re.sub(('(.%s)'%{3*len(g[0])-3*len((s+g)[0])+4}).join(re.sub(str(m),str(B),str(s)[1:-1])for s in s),''.join(f'\g<{(i:=i+1)}>'*(i>0)+str(s)[1:-1]for s in s),str(g)))
 return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]
