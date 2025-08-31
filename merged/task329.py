# att (54 bytes, gold)
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]

### ovs (tied, 54 bytes)
p=lambda g:[[0]*(n:=len(r)//2)+[r[n]]+n*[0]for r in g]

### xsot (tied, 54 bytes)
p=lambda m:[[0]*(x:=len(m)//2)+[l[x]]+x*[0]for l in m]

### combined (tied, 54 bytes)
p=lambda i:[(r:=len(x)//2)*[0]+[x[r]]+r*[0]for x in i]
