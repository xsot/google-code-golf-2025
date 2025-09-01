# combined (171 bytes, gold)
p=lambda i,k=3,s=0:-k*i or p([[y or(s==5in{*(h:=[*map(max,i)])[b+1:]}&{*h[:b]})*sum({*sum(i,[])},-5)for b,y in enumerate(x)]*1**(s:=s*2+max(x))for x in zip(*i)][::-1],k-1)

### ovs (214 (218 unzipped) bytes)
def p(g):E=enumerate;(y,*_,Y),(x,*_,X)=map(sorted,zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]));f=sum(g,[]);c,={*f}-{0,5};return[[v|c*((x<j<X)*(i in{y+1,Y-1})|(y<i<Y)*(j in{x+1,X-1}))for j,v in E(r)]for i,r in E(g)]
