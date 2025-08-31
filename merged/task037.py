# ovs (109 vs 107 bytes for gold)
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]

### combined (tied, 109 bytes)
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]
