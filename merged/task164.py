# att (32 vs 2500 bytes for gold)
p=lambda a:[b+b[::-1]for b in a]

### ovs (tied, 32 bytes)
p=lambda g:[r+r[::-1]for r in g]

### xsot (tied, 32 bytes)
p=lambda m:[r+r[::-1]for r in m]

### combined (tied, 32 bytes)
p=lambda i:[x+x[::-1]for x in i]
