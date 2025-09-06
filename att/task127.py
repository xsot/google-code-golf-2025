p=eval('lambda a:[[sum(sum(a,()))%5+5'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)

##
p=eval('lambda a:[[sum({*sum(a,()),5})'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)
p=lambda a:[*map(f:=lambda*b:[sum(c)%5+5for*c,in zip((0,)+b,b,b[1:]+b)],*map(f,*a))]
p=lambda a:[*map(f:=lambda*b:sum(([5]+3*[e%5+5]for e in b[1::4]),[])[1:],*map(f,*a))]