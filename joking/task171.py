p=lambda a:a*all(a[0])or p([*zip(*a[:0:-1],[8]*9)])

##
p=lambda a,k=3:-k*a or[*zip(*p(a,k-1)[:0:-1],[8]*9)]