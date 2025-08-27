p=lambda a:[[[5,c][c==max(d:=sum(a,a),key=d.count)]for c in b]for b in a]

### ovs (74 bytes)
p=lambda g:[[[5,v][v==max(f:=sum(g,[]),key=f.count)]for v in r]for r in g]

### xsot (74 bytes)
p=lambda m:[[[5,v][v==max(a:=sum(m,[]),key=a.count)]for v in l]for l in m]
