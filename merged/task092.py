# combined (99 vs 87 bytes for gold)
p=lambda i,*n:[[y or max({*x[b:],0}&{*x[:b],0})for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
