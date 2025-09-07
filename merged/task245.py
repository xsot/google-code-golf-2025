# ovs (117 vs 106 bytes for gold)
p=lambda i,k=15:-k*i or p([[v%2*v|w%3for v,w in zip(r,[0]*(2in{*max(i,key=any)}&{*r})+r)]for*r,in zip(*i)][::-1],k-1)

## fails a single case:

p=lambda i,k=15:-k*i or p([([0]*(2in{*max(i,key=any)}&{*r})+r)[:len(r)]for*r,in zip(*i)][::-1],k-1)

### combined (142 bytes)
p=lambda i,k=15:-k*i or p([[y[1]%2*3or y[(f:=sum(i,[]).index)(3)//(w:=len(i[0]))<f(2)//w]%3for y in zip([0,*x],x)]for x in zip(*i)][::-1],k-1)
