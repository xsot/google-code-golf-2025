# joking+mwi (45 vs 42 bytes for gold)
p=lambda g:([max(g[::3]),*g[4:6]]*9)[:len(g)]

### att (46 bytes)
p=lambda a:[max((a:=a[:2]+a)[2::3])for _ in a]

### ovs (48 bytes)
p=lambda g,i=2:[max(g[(i:=i+1)%3::3])for _ in g]

### xsot (48 bytes)
p=lambda m,i=0:m[i:]and[max(m[i%3::3])]+p(m,i+1)
##
p=lambda m:[max(m[i%3::3])for i in range(len(m))]
