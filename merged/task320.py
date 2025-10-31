# ovs (66 vs 65 bytes for gold)
p=lambda a:[*zip(*[c[:-(w:=sum(c)//4)]+w*[8]+c for*c,in zip(*a)])]

### att (72 bytes)
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]

### combined (72 bytes)
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]
