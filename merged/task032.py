# att (39 vs 2500 bytes for gold)
p=lambda a:[*zip(*map(sorted,zip(*a)))]

### ovs (tied, 39 bytes)
p=lambda g:[*zip(*map(sorted,zip(*g)))]

### xsot (tied, 39 bytes)
p=lambda m:[*zip(*map(sorted,zip(*m)))]

### combined (tied, 39 bytes)
p=lambda i:[*zip(*map(sorted,zip(*i)))]
