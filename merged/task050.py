# combined (96 vs 86 bytes for gold)
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]

### ovs (tied, 96 bytes)
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]
