# ovs (46 bytes, gold)
p=lambda a:a>a*0!=0and[p(a[1])]*4+p(a[2:])or a

##

p=lambda g:sum([[sum([4*[v]for v in r[1::2]],[])]*4for r in g[1::2]],[])

### att (58 bytes)
p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)

### combined (58 bytes)
p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)
