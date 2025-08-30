# att (42 vs 39 bytes for gold)
p=lambda a:[3*[-b.index(5)%3+2]for b in a]

### ovs (tied, 42 bytes)
p=lambda g:[3*[2+-r.index(5)%3]for r in g]

### xsot (tied, 42 bytes)
p=lambda m:[3*[-r.index(5)%3+2]for r in m]
