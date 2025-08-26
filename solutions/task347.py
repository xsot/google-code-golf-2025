p=lambda m:[[c+r.pop(3)and 6for c in r]for r in m]
##
p=lambda m:[[6*any(r[c::3])for c in[0,1,2]]for r in m]
p=lambda m:[[6*any(c)for c in zip(r,r[3:])]for r in m]

### ovs (tied, {ovs_score} bytes)
p=lambda g:[[6>>r.pop(3)+b^6for b in r]for r in g]
