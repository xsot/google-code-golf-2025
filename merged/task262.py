# combined (39 vs 2500 bytes for gold)
p=lambda i:[[~b//~a^2]*3for a,b,_ in i]

### att (42 bytes)
p=lambda a:[3*[-b.index(5)%3+2]for b in a]

### ovs (42 bytes)
p=lambda g:[3*[2+-r.index(5)%3]for r in g]

### xsot (42 bytes)
p=lambda m:[3*[-r.index(5)%3+2]for r in m]
