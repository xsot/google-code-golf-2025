# joking (85 bytes, gold)
p=lambda a,*b,s=0:[c|(s&(s:=s^c)&~sum(b))//8*3for c in b]or[*map(p,a,*map(p,a*9,*a))]

### ovs (tied, 85 bytes)
p=lambda a:[*map(f:=lambda*b,s=0:[c|(s&(s:=s^c)&~sum(b))//8*3for c in b],*map(f,*a))]

### att (91 bytes)
p=lambda a:[*map(f:=lambda*b,i=0:[c|3*(8in{*b[:i]}&{*b[(i:=i+1):]})for c in b],*map(f,*a))]

### combined (96 bytes)
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]
