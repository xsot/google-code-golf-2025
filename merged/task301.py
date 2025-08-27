p=lambda g,S=sorted:S(map(S,g))

### xsot (tied, 31 bytes)
p=lambda m,s=sorted:s(map(s,m))

### att (32 bytes)
p=lambda a:sorted(map(sorted,a))
