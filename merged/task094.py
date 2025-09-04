# joking (106 bytes, gold)
p=lambda i,*h:[h:=[(y>2==x.count((c:=h.count)(1)%5-1)>=c(6))*6or y for y in x]for x in zip(*h or p(i,*i))]

### combined (137 bytes)
p=lambda i,k=1:-k*i or p([[(y>7>x.count(1)<3==sum([*zip(*i)][a-1:a+2],x).count(1)%5)*6or y for y in x]for a,x in enumerate(zip(*i))],k-1)
