# att (54 bytes, gold)
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]

### combined (tied, 54 bytes)
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]

### xsot (93 bytes)
p=lambda m:len(set(r:=m[0]))>1and[[c for c,d in zip(r,[0,*r])if c^d]]or[*zip(*p([*zip(*m)]))]
###
p=lambda m:len(set(r:=m[0]))>1and[[c for c,d in zip(r,[0,*r])if c^d]]or[*zip(*p([*zip(*m)]))]
p=lambda m:len({*m[0]})>1and[[c for c,d in zip(m[0],[0,*m[0]])if c^d]]or[*zip(*p([*zip(*m)]))]
