# att (91 bytes, gold)
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[len(a)//2+1:])]'*2)

### combined (104 bytes)
p=lambda i:[p:=len(i)//2+1]and[[min(y,key=y.count)for y in zip(x,t,x[p:],t[p:])]for x,t in zip(i,i[p:])]
