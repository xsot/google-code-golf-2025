# ovs (93 bytes, gold)
p=lambda a,m=9:[*zip(*{(d,)*m:0for d in sum(zip(*a),())if sum(a,[]).count(d)==m})]or p(a,m-1)

### att (96 bytes)
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]

### combined (96 bytes)
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]
