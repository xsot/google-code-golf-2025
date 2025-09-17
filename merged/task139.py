# joking (89 bytes, gold)
p=lambda i,k=4,*w:k and p([*map(p,i,[k>1]*99,i[:1]+i,i[1:]+i,*w)],k-1)or i or(sum(w)>7)*7

### ovs (94 bytes)
p=lambda i,v=11:-v*i or[[q+(v&(v:=v*2+q%3)>>9&1>>q)*7for q in r]for r in zip(*p(i,v-1)[::-1])]

### combined (100 bytes)
p=lambda i,k=11,r=range(9):-k*i or p([[i[~b][a]or i[-b][a]*i[~b][a-1]%3*7for b in r]for a in r],k-1)

### xsot (102 bytes)
import re
p=lambda m,i=11:-i*m or[*zip(*eval(re.sub("0(?=, [^0].{25}[^0])","7",str(p(m,i-1)[::-1]))))]
