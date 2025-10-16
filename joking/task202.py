p=lambda a:[[*map(min,*[c for c in a if{*c}<=r])]for b in a if len(r:={*b,0})<3]or[*zip(*p([*zip(*a)]))]

##
p=lambda a:[[*map(min,*[c for c in a if max(b)in c])]for b in(len({*a[0],0})<3)*a]or[*zip(*p([*zip(*a)]))]