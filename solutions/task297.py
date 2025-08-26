p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]*2]
###
p=lambda m:m[:2]+[[c]*len(m[0])for c in m[0]]*2

### ovs (tied, {ovs_score} bytes)
p=lambda g:g[:2]+[len(g[0])*[v]for v in g[0]*2]
