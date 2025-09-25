# joking (59 bytes, gold)
p=lambda i,*n:sorted(n,key=0 .__eq__)or[*zip(*map(p,i,*i))]

### combined (61 bytes)
p=lambda i:[*zip(*[sorted(x,key=0 .__eq__)for x in zip(*i)])]

### ovs (65 bytes)
p=lambda g:[[c[c.count(1)+~i]for*c,in zip(*g)]for i in range(10)]
##
p=lambda i:[*zip(*[[v%2or n.pop()for v in n*1]for*n,in zip(*i)])]
