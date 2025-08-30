# att (67 bytes, gold)
p=lambda a,c=0:[(b:=0)or[c:=(b:=b or d)for d in r+[c]]for*r,_ in a]

### ovs (76 bytes)
p=lambda g,l=0:[[k:=k|v for v in r[:-1]]+[l:=max(r)or l]for r in g if[k:=0]]
