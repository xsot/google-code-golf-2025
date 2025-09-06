# joking (81 vs 73 bytes for gold)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]

### combined (tied, 81 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]
