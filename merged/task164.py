# att (32 bytes, gold)
p=lambda a:[b+b[::-1]for b in a]

### combined (tied, 32 bytes)
p=lambda i:[x+x[::-1]for x in i]

### ovs (tied, 32 bytes)
p=lambda g:[r+r[::-1]for r in g]

### xsot (tied, 32 bytes)
p=lambda m:[r+r[::-1]for r in m]
