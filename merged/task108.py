p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)

### ovs (72 bytes)
p=lambda g:sum([[sum([4*[v]for v in r[1::2]],[])]*4for r in g[1::2]],[])
