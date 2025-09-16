# joking (61 vs 58 bytes for gold)
p=lambda i:[(e:=0)or[(e:=y-e)>>9&5or e for y in x]for x in i]

##
p=lambda i:[(e:=0)or[max(e:=y-e,e>>9&5)for y in x]for x in i]

### combined (63 bytes)
p=lambda i:[[(0>(e:=y-e))*5or e for y in x]for x in i if[e:=0]]

### att (67 bytes)
p=lambda a:[(c:=0)or[c:=e or c and 5^c^sum(b)for e in b]for b in a]

### ovs (73 bytes)
p=lambda g:[[(f:=f^(c>0))*5or(c:=c|v)for v in r]for r in g if[c:=0,f:=0]]
