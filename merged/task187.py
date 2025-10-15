# joking (88 bytes, gold)
p=lambda i,k=7:-k*i or[*map(lambda*x,z=3:[z:=y|(y*z==6)or 2for y in x],*p(i,k-1)[::-1])]

### att (89 bytes)
p=lambda i,k=59:-k*i or[*map(lambda*x,z=3:[z:=y|(y*z==6)or 2for y in x],*p(i,k-1)[::-1])]

### ovs (91 bytes)
p=lambda i,k=59:-k*i or[*map(lambda*x,z=3:[y|(z*(z:=y)==6)or 2for y in x],*p(i,k-1)[::-1])]

### combined (107 bytes)
p=lambda i,k=79:-k*i or[[y*(y!=2)or(z==3)*3or y or 2for y,z in zip(x,[3,*x])]for x in zip(*p(i,k-1)[::-1])]
