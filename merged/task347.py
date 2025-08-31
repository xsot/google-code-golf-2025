# att (50 bytes, gold)
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]

### combined (tied, 50 bytes)
p=lambda i:[[y+x.pop(3)and 6for y in x]for x in i]

### ovs (tied, 50 bytes)
p=lambda g:[[6>>r.pop(3)+b^6for b in r]for r in g]

### xsot (tied, 50 bytes)
p=lambda m:[[c+r.pop(3)and 6for c in r]for r in m]
##
p=lambda m:[[6*any(r[c::3])for c in[0,1,2]]for r in m]
p=lambda m:[[6*any(c)for c in zip(r,r[3:])]for r in m]
