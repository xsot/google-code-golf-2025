# ovs (31 vs 2500 bytes for gold)
p=lambda g,S=sorted:S(map(S,g))

### xsot (tied, 31 bytes)
p=lambda m,s=sorted:s(map(s,m))

### combined (tied, 31 bytes)
p=lambda i,s=sorted:s(map(s,i))

### att (32 bytes)
p=lambda a:sorted(map(sorted,a))
