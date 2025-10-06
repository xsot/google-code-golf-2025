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