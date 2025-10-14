# joking (64 bytes, gold)
p=lambda a,q=3:5+a%5if-1*a else a[1:]and[p(a[1])]*q+p(a[2:],4-q)

### ovs (65 bytes)
p=lambda a,q=3:a*0==0and 5+a%5or a[1:]and[p(a[1])]*q+p(a[2:],4-q)

##

p=eval('lambda a:[[sum(b"%r0"%a)%5+5'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)

### att (80 bytes)
p=eval('lambda a:[[sum(sum(a,()))%5+5'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)

##
p=eval('lambda a:[[sum({*sum(a,()),5})'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)
p=lambda a:[*map(f:=lambda*b:[sum(c)%5+5for*c,in zip((0,)+b,b,b[1:]+b)],*map(f,*a))]
p=lambda a:[*map(f:=lambda*b:sum(([5]+3*[e%5+5]for e in b[1::4]),[])[1:],*map(f,*a))]

### combined (82 bytes)
p=lambda i,E=enumerate:[[5+(y<5)*i[a&12|1][b&12|1]for b,y in E(x)]for a,x in E(i)]
