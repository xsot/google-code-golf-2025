# combined (50 bytes, gold)
p=lambda i:[f:=i[0],[*map(max,f[1:]+[0],[0]+f)]]*3

### ovs (tied, 50 bytes)
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3

### att (55 bytes)
p=lambda a:[b:=a[0],[*map(sum,zip(b[1:]+[0],[0]+b))]]*3
