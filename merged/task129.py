# att (47 bytes, gold)
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3

### ovs (48 bytes)
p=lambda g:[[max(f:=sum(g,[]),key=f.count)]*3]*3

### xsot (48 bytes)
p=lambda m:[[max(a:=sum(m,[]),key=a.count)]*3]*3
