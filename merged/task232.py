# joking (57 bytes, gold)
p=lambda i,e=0:i*0!=0and[p(y)or[e:=y-e,5][e<0]for y in i]

##
p=lambda i:[(e:=0)or[max(e:=y-e,e>>9&5)for y in x]for x in i]
p=lambda i:[(e:=0)or[(e:=y-e)>>9&5or e for y in x]for x in i]

### ovs (58 bytes)
p=lambda i:[(e:=0)or[[e:=y-e,5][e<0]for y in x]for x in i]

##

p=lambda g:[[(f:=f^(c>0))*5or(c:=c|v)for v in r]for r in g if[c:=0,f:=0]]

### combined (63 bytes)
p=lambda i:[[(0>(e:=y-e))*5or e for y in x]for x in i if[e:=0]]

### att (67 bytes)
p=lambda a:[(c:=0)or[c:=e or c and 5^c^sum(b)for e in b]for b in a]
