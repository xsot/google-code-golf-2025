p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]

### ovs (74 bytes)
p=lambda g:[[v for*c,v in zip(*g,r)if any(c)][:3]for r in g if any(r)][:3]
