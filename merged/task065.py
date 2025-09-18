# att (84 bytes, gold)
p=lambda a:[p(b)for*b,in map(zip,a,a[len(a)//2+1:])]or min(b:=sum(a,()),key=b.count)

### combined (104 bytes)
p=lambda i:[p:=len(i)//2+1]and[[min(y,key=y.count)for y in zip(x,t,x[p:],t[p:])]for x,t in zip(i,i[p:])]
