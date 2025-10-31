# joking (104 vs 101 bytes for gold)
import re;p=lambda g,k=9:-k*g or p(eval(re.sub(r"(?<=(.).{28})(?=(.{29})+\1)0",r"\1",str(g)))[::-1],k-1)

##
import re;p=lambda g,k=9:-k*g or p(eval(re.sub(r"(?<=(.).{34})(?=(.{35})+\1)0",r"\1",str(g)))[::-1],k-1)
import re;p=lambda g:exec(r'g[::-1]=eval(re.sub(r"(?<=(.).{34})(?=(.{35})+\1)0",r"\1",str(g)));'*10)or g

### ovs (109 bytes)
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]

### combined (109 bytes)
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]
