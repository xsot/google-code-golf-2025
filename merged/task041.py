# att (49 bytes, gold)
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]

### ovs (tied, 49 bytes)
p=lambda g,p=0:[[v|(p:=v^p)for v in r]for r in g]
