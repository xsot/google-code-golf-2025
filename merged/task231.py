# att (43 bytes, gold)
p=lambda a:[(r[:6]*4)[:len(r)*2]for r in a]

### ovs (tied, 43 bytes)
p=lambda g:[(r[:6]*4)[:len(r*2)]for r in g]

### xsot (tied, 43 bytes)
p=lambda m:[(r[:6]*9)[:len(r)*2]for r in m]

### combined (tied, 43 bytes)
p=lambda i:[(x[:6]*4)[:len(x)*2]for x in i]
