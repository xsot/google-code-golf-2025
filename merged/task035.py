# combined (87 vs 2500 bytes for gold)
p=lambda i,k=3:-k*i or[[x[0**k<=(k:=y)^8]or y for y in x]for x in zip(*p(i,k-1)[::-1])]

### ovs (108 bytes)
p=lambda g:[g:=[[r[0]*(s^(s:=s|{v})=={8})or v for v in r]for*r,in zip(*g[::-1])if(s:={0})]for _ in' '*4][-1]
