# ovs (48 vs 2500 bytes for gold)
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]

### combined (tied, 48 bytes)
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]

### xsot (51 bytes)
p=lambda m:[l[:1]*5+[l[0]and 5]+l[10:]*5for l in m]
##
p=lambda m:[l[:1]*5+[l[0]and 5]+l[10:]*5for l in m]
p=lambda m:[[l[0]]*5+[l[0]and 5]+[l[10]]*5for l in m]
p=lambda m:[l[0]and[l[0]]*5+[5]+[l[10]]*5or l for l in m]
