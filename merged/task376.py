p=lambda a:(a+a[1:-1])*2+a[:1]

### xsot (tied, 30 bytes)
p=lambda x:(x+x[1:-1])*2+x[:1]
##
p=lambda x:(x+x[1:-1])*2+[x[0]]
p=lambda x:(y:=x+x[::-1][1:])+y[1:]

### ovs (33 bytes)
p=lambda g:(e:=g+g[-2::-1])+e[1:]
