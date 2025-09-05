# mwi (63 vs 2500 bytes for gold)
p=lambda i,r=range(18):[[y*x%max(i[~0])+1for y in r]for x in r]

### joking (64 bytes)
p=lambda i,r=range(18):[[y*x%max(max(i))+1for y in r]for x in r]

### combined (93 bytes)
p=lambda i,k=7:-k*i or[[*map(max,x,x[:len({*sum(i,[0])})-1]*9)]for x in zip(*p(i,k-1))][::-1]

### att (101 bytes)
p=lambda a:min([*map(f:=lambda*b:[max(b[i%n::n])for i in range(18)],*map(f,*a))]for n in range(5,10))
