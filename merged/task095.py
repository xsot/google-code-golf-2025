# att (75 vs 73 bytes for gold)
p=lambda a,n=6:~n*a or[[n%2|(n:=b.pop())for _ in a]for*b,in zip(*p(a,n-2))]

### joking (81 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]

### combined (81 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]
