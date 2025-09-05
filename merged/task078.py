# combined (61 vs 2500 bytes for gold)
p=lambda i:[*zip(*[sorted(x,key=0 .__eq__)for x in zip(*i)])]

### ovs (65 bytes)
p=lambda g:[[c[c.count(1)+~i]for*c,in zip(*g)]for i in range(10)]
