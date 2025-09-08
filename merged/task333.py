# att (92 vs 89 bytes for gold)
p=lambda a,n=-3:n*a or[(d:=0)or[d:=b.pop()|d*(3in b[:-1])for _ in a]for*b,in zip(*p(a,n+1))]

### combined (93 bytes)
p=lambda a,n=-23:n*a or[(d:=0)or[d:=b.pop()|d*(3in b[:-1])for _ in a]for*b,in zip(*p(a,n+1))]
