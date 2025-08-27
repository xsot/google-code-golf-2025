p=lambda g:[[*filter(abs,r)][::-1]for r in g if any(r)]

### xsot (tied, 55 bytes)
p=lambda m:[[*filter(int,l[::-1])]for l in m if sum(l)]
##
p=lambda m,F=filter:[[*F(int,l[::-1])]for l in F(sum,m)]
p=lambda m:[[*filter(None,l)][::-1]for l in filter(sum,m)]
p=lambda m:[[i for i in l[::-1]if i]for l in filter(sum,m)]
