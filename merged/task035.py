# att (84 vs 83 bytes for gold)
p=lambda i,k=3:-k*i or[[i[k>(k:=y)%9-8]or k for y in i]for i[::-1]in zip(*p(i,k-1))]

### ovs (85 bytes)
p=lambda i,k=3:-k*i or[[x[k>(k:=y)%9-8]or k for y in x]for x in zip(*p(i,k-1)[::-1])]

##

p=lambda g:[g:=[eval(str(r).replace(*f'8{r[0]}',r[0]>0))for r in zip(*g)][::-1]for _ in g][3]
p=lambda g:[g:=[[r[0]*(s^(s:=s|{v})=={8})or v for v in r]for*r,in zip(*g[::-1])if(s:={0})]for _ in' '*4][-1]

### combined (87 bytes)
p=lambda i,k=3:-k*i or[[x[0**k<=(k:=y)^8]or y for y in x]for x in zip(*p(i,k-1)[::-1])]
