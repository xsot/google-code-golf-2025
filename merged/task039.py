# att (60 bytes, gold)
p=lambda a,n=7:-n*a[:3]or p([*zip(*a[1-any(a[0]):3+n])],n-1)

##
p=lambda a,n=7:-n*a or p([*zip(*a[1-any(a[n<1]):2+n|1])],n-1)

### joking (61 bytes)
p=lambda a,f=filter:[*zip(*[*f(any,zip(*f(any,a)))][:3])][:3]

### ovs (64 bytes)
p=lambda a,k=-1:k*a or[*zip(*p([*filter(any,zip(*a))],k+1))][:3]

##

p=lambda g:[[v for*c,v in zip(*g,r)if any(c)][:3]for r in g if any(r)][:3]

### combined (65 bytes)
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]
