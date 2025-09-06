# att (95 vs 86 bytes for gold)
p=lambda a:[*map(f:=lambda*b:[c|3*(8in{*b[:i]}&{*b[i+1:]})for i,c in enumerate(b)],*map(f,*a))]

### ovs (96 bytes)
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]

### combined (96 bytes)
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]
