p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]

### ovs (99 bytes)
def p(g):f=sum(zip(*g),());m=max(map(q:=f.count,{*f}-{0}));return[[*{c:0 for c in f if q(c)==m}]]*m
