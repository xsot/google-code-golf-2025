# att (33 vs 2500 bytes for gold)
p=lambda a:[b[:len(a)]for b in a]

### ovs (tied, 33 bytes)
p=lambda g:[r[:len(g)]for r in g]

### xsot (tied, 33 bytes)
p=lambda m:[r[:len(m)]for r in m]

### combined (tied, 33 bytes)
p=lambda g:[r[:len(g)]for r in g]
