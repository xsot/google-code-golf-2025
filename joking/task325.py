p=lambda i,k=39,z=8:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[s:=h and(h<9)*(z:=z*2)+s|h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)


##
p=lambda i,k=39,z=0:-k*[r:=range(len({*sum(i,[])})-1)]and[[(y==x)*8for y in r]for x in r]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
p=lambda i,k=39,r=0,z=0:-k*[[(y==x)*8for y in r]for x in r]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1,range(len({*sum(i,[])})-1))
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([[(k<39)*h[0]and max(h)or(z:=z+1)*h[0]for h in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h*[s,s:=h]+[0])or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[k//39*h*(z:=z+1)or max(h and s,s:=h)for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(h==8)*(z:=z+1)+max(h and s,s:=h)for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)