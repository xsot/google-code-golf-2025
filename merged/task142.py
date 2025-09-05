# att (40 vs 2500 bytes for gold)
p=lambda a:[b+b[::-1]for b in a+a[::-1]]

### ovs (tied, 40 bytes)
p=lambda g:[r+r[::-1]for r in g+g[::-1]]

### xsot (tied, 40 bytes)
p=lambda m:[l+l[::-1]for l in m+m[::-1]]

### combined (tied, 40 bytes)
p=lambda i:[x+x[::-1]for x in i+i[::-1]]
