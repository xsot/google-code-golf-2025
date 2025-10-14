# att (111 bytes, gold)
p=lambda i,k=-99:k*i or p([*map(lambda*r,a=8:[[b%5,b or 8&a,b|2*(a%3<(a:=b))][k//50]for b in r],*i[::-1])],k+1)

### ovs (112 bytes)
p=lambda i,k=-99:k*i or p([*map(lambda*r,a=-4:[[b%4,b or-4&a,b|2*(a%3<(a:=b))][k//50]for b in r],*i[::-1])],k+1)

##

p=lambda i,k=79:-k*i or p([[(k<32>y==1<s)*3or~-(k<32>y==4)*y*~-(s<1>y%2)or k//79*4for s,y in zip([0]+x,x)]for*x,in zip(*i[::-1])],k-1)

### combined (135 bytes)
p=lambda i,k=79:-k*i or p([[(k<32>y==1<s)*3or~-(k<32>y==4)*y*~-(s<1>y%2)or k//79*4for s,y in zip([0,*x],x)]for x in zip(*i[::-1])],k-1)
