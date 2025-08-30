# att (46 bytes, gold)
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]

### combined (tied, 46 bytes)
p=lambda g:g[:1]*3+[g[3],[5-c*4for c in g[2]]]

### ovs (tied, 46 bytes)
p=lambda g:g[:1]*3+[g[3],[5^v*4for v in g[2]]]

### xsot (tied, 46 bytes)
p=lambda m:m[:1]*3+[m[3],[5-c*4for c in m[2]]]
##
p=lambda m:m[:1]*3+[m[3],[c or 5 for c in m[2]]]
