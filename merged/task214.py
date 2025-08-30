# att (63 vs 62 bytes for gold)
p=lambda a:[b[:4]+c[::-1]+a.pop()[3::-1]for*c,b in[*zip(*a,a)]]

### joking+mwi (tied, 63 bytes)
p=lambda a:[b[:4]+c[::-1]+a.pop()[3::-1]for*c,b in[*zip(*a,a)]]

### ovs (73 bytes)
p=lambda g:[a[:3]+[5,*b,5]+c[2::-1]for a,*b,c in zip(g,*g[::-1],g[::-1])]
