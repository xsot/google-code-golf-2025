p=lambda a:[[*map(min,*[c for c in a if max(b)in c])]for b in a if len({*b,0})<3]or[*zip(*p([*zip(*a)]))]

##

def p(g):
 for _ in'..':
  *_,P=g=[*map(list,zip(*g))]
  for r in g:
   for x,v in zip(P,P:=r*(len({*r}-{0})>1)):r[:]=[n*(v>0 or n!=x)for n in r]
 return g
