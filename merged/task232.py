# att (67 vs 58 bytes for gold)
p=lambda a:[(c:=0)or[c:=e or c and 5^c^sum(b)for e in b]for b in a]

### ovs (73 bytes)
p=lambda g:[[(f:=f^(c>0))*5or(c:=c|v)for v in r]for r in g if[c:=0,f:=0]]
