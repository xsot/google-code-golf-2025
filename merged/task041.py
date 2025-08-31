# att (49 bytes, gold)
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]

### combined (tied, 49 bytes)
p=lambda i,l=0:[[y|(l:=l^y)for y in x]for x in i]

### ovs (tied, 49 bytes)
p=lambda g,p=0:[[v|(p:=v^p)for v in r]for r in g]
