# mwi (43 vs 59 bytes for gold)
p=lambda a:a==5or a and[p(a[1])]*3+p(a[3:])

### ovs (48 bytes)
p=lambda a:a>a*0==0 or a and[p(a[1])]*3+p(a[3:])

### att (59 bytes)
p=eval('lambda a:[[a>0'+"for a in a[1::3]for _ in'   ']"*2)

### combined (59 bytes)
p=lambda i,r=b"":[[i[a][b]>0for b in r]for a in r]
