# att (39 vs 2500 bytes for gold)
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]

### xsot (tied, 39 bytes)
p=lambda m:[l:=[*zip(*m)][0]*3,l[::-1]]

### combined (tied, 39 bytes)
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]

### ovs (42 bytes)
p=lambda g:[r:=[*[*zip(*g)][0]]*3,r[::-1]]
