# att (37 vs 2500 bytes for gold)
p=lambda a:[[*filter(int,sum(a,[]))]]

### ovs (tied, 37 bytes)
p=lambda g:[[*filter(abs,sum(g,[]))]]

### xsot (tied, 37 bytes)
p=lambda m:[[*filter(int,sum(m,[]))]]

### combined (tied, 37 bytes)
p=lambda i:[[*filter(int,sum(i,[]))]]
