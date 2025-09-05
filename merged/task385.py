# att (25 vs 2500 bytes for gold)
p=lambda a:a[:4:-1]+a[5:]

### ovs (tied, 25 bytes)
p=lambda g:g[:4:-1]+g[5:]

### xsot (tied, 25 bytes)
p=lambda m:m[:4:-1]+m[5:]

### combined (tied, 25 bytes)
p=lambda i:i[:4:-1]+i[5:]
