# ovs (50 vs 2500 bytes for gold)
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3

### combined (tied, 50 bytes)
p=lambda i:[f:=i[0],[*map(max,f[1:]+[0],[0]+f)]]*3

### att (55 bytes)
p=lambda a:[b:=a[0],[*map(sum,zip(b[1:]+[0],[0]+b))]]*3
