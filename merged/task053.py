# att (21 vs 2500 bytes for gold)
p=lambda a:(a+a)[2:5]

### ovs (tied, 21 bytes)
p=lambda g:(g*2)[2:5]

### xsot (tied, 21 bytes)
p=lambda m:(m*2)[2:5]
##
p=lambda m:[m.pop()]+m

### combined (tied, 21 bytes)
p=lambda i:(i*2)[2:5]
