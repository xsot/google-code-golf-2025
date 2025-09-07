# ovs (106 vs 94 bytes for gold)
p=lambda i,k=79:-k*i or[[y*(y!=2)or(z==3)*3or y or 2for y,z in zip(x,[3]+x)]for*x,in zip(*p(i,k-1)[::-1])]

### combined (107 bytes)
p=lambda i,k=79:-k*i or[[y*(y!=2)or(z==3)*3or y or 2for y,z in zip(x,[3,*x])]for x in zip(*p(i,k-1)[::-1])]
