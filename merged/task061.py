# combined (93 vs 63 bytes for gold)
p=lambda i,k=7:-k*i or[[*map(max,x,x[:len({*sum(i,[0])})-1]*9)]for x in zip(*p(i,k-1))][::-1]

### att (101 bytes)
p=lambda a:min([*map(f:=lambda*b:[max(b[i%n::n])for i in range(18)],*map(f,*a))]for n in range(5,10))
