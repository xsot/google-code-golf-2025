# ovs (75 vs 2500 bytes for gold)
p=lambda i,k=7:-k*i or[[*map(max,x,[0]*10+x)]for*x,in zip(*p(i,k-1))][::-1]

### combined (81 bytes)
p=lambda i,k=7:-k*i or[[*x[:10],*map(max,x,x[10:])]for x in zip(*p(i,k-1))][::-1]

### att (82 bytes)
p=lambda a:[*map(f:=lambda*b:[max(b[i%10::10])for i in range(len(b))],*map(f,*a))]
