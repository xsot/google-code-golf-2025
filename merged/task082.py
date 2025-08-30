# att (50 bytes, gold)
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3

### att (55 bytes)
p=lambda a:[b:=a[0],[*map(sum,zip(b[1:]+[0],[0]+b))]]*3
