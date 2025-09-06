# joking (106 vs 102 bytes for gold)
p=lambda a:[[*map(min,*[c for c in a if max(b)in c])]for b in(len({*a[0],0})<3)*a]or[*zip(*p([*zip(*a)]))]

### att (109 bytes)
p=lambda a:(len({*a[0]}-{0})<2)*[[*map(min,*[c for c in a if max(b)in c])]for b in a]or[*zip(*p([*zip(*a)]))]

### combined (109 bytes)
p=lambda a:(len({*a[0]}-{0})<2)*[[*map(min,*[c for c in a if max(b)in c])]for b in a]or[*zip(*p([*zip(*a)]))]

### ovs (155 bytes)
def p(g):
 for _ in'..':
  *_,P=g=[*map(list,zip(*g))]
  for r in g:
   for x,v in zip(P,P:=r*(len({*r}-{0})>1)):r[:]=[n*(v>0 or n!=x)for n in r]
 return g
