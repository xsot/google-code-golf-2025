# att (79 vs 73 bytes for gold)
p=lambda i,k=3,z=0:-k*i or[[z%4|(z:=x.pop())for _ in i]for*x,in zip(*p(i,k-1))]

### joking (81 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]

### combined (81 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]
