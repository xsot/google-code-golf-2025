# combined (75 vs 2500 bytes for gold)
p=lambda i:(s:=[a+x for a,*x in zip(i,*i[::-1])])+[x[::-1]for x in s[::-1]]

### ovs (76 bytes)
p=lambda g,*x:[x:=[w:=a+b[::-1],*x,w[::-1]]for*b,a in[*zip(*g,g)][::-1]][-1]
