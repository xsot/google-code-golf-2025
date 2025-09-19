# joking (96 bytes, gold)
p=lambda i:[i:=[[(y==5)*c[c[1]>0]or y for*c,y in zip([0]+x,*i,x)][::-1]for x in i]for x in i][9]

## some recursive experiments
p=lambda i,*c:(i==5)*c[c[1]>0]or i if c else[i:=[[*map(p,x,[0]+x,*i)][::-1]for x in i]for x in i][9]
p=lambda i,k=10,*c:((i==5)*(c[0]or k)if c else k and p([[*map(p,x,[0]+x,*i)][::-1]for x in i],k-1))or i

### mwi (99 bytes)
p=lambda i:[i:=[[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0]+x)][::-1]for x in i]for x in i][9]

### ovs (100 bytes)
p=lambda i,k=9:-k*i or p([[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0]+x)][::-1]for x in i],k-1)

### combined (101 bytes)
p=lambda i,k=9:-k*i or p([[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0,*x])][::-1]for x in i],k-1)

### att (105 bytes)
p=lambda a:[*map(f:=lambda b,c=a[0]:b and(d:=[*b,0].index(0)or 1)*[b[0]and max(c[:d])]+f(b[d:],c[d:]),a)]
