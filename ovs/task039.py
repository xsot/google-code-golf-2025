p=lambda a,k=-1:k*a or[*zip(*p([*filter(any,zip(*a))],k+1))][:3]

##

p=lambda g:[[v for*c,v in zip(*g,r)if any(c)][:3]for r in g if any(r)][:3]
