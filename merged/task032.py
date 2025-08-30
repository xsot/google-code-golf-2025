# att (39 bytes, gold)
p=lambda a:[*zip(*map(sorted,zip(*a)))]

### combined (tied, 39 bytes)
p=lambda i:[*zip(*map(sorted,zip(*i)))]

### ovs (tied, 39 bytes)
p=lambda g:[*zip(*map(sorted,zip(*g)))]

### xsot (tied, 39 bytes)
p=lambda m:[*zip(*map(sorted,zip(*m)))]
