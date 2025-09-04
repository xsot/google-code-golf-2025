# ovs (100 vs 97 bytes for gold)
p=lambda i,k=9:-k*i or p([[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0]+x)][::-1]for x in i],k-1)

### combined (101 bytes)
p=lambda i,k=9:-k*i or p([[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0,*x])][::-1]for x in i],k-1)

### att (105 bytes)
p=lambda a:[*map(f:=lambda b,c=a[0]:b and(d:=[*b,0].index(0)or 1)*[b[0]and max(c[:d])]+f(b[d:],c[d:]),a)]
