# ovs (64 vs 60 bytes for gold)
p=lambda a,k=-1:k*a or[*zip(*p([*filter(any,zip(*a))],k+1))][:3]

##

p=lambda g:[[v for*c,v in zip(*g,r)if any(c)][:3]for r in g if any(r)][:3]

### att (65 bytes)
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]

### combined (65 bytes)
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]
