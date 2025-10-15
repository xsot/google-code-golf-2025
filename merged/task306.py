# ovs (69 bytes, gold)
p=lambda i:[i:=[*zip(*map(max,i,i[10:]+i[9:]+i))][::-1]for _ in i][7]

### combined (81 bytes)
p=lambda i,k=7:-k*i or[[*x[:10],*map(max,x,x[10:])]for x in zip(*p(i,k-1))][::-1]

### att (82 bytes)
p=lambda a:[*map(f:=lambda*b:[max(b[i%10::10])for i in range(len(b))],*map(f,*a))]
