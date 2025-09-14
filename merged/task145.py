# ovs (191 bytes, gold)
p=lambda x,k=79,v=2:-k*x or p([[(k and a|(b or(v:=v*2))or max(h:={*map(C:=(f:=sum(x,[])).count,{*f}-{2})})==C(b)or(C(b)==min(h))*8,b)[b==2]for a,b in zip([0]+r,r)]for*r,in zip(*x[::-1])],k-1)

## this (barely?) exceeds recursion limit. passes on my testing notebook:

p=lambda x,k=3:-k*x or p([[(max(a,b or(k:=k+4))*(k>0)or max(h:={*map(C:=(f:=sum(x,[])).count,{*f}-{2})})==C(b)or(C(b)==min(h))*8,b)[b==2]for a,b in zip([0]+r,r)]for*r,in zip(*x[::-1])],k-1)

### combined (199 bytes)
p=lambda i,k=79,t=0:-k*i or p([[{*0**y*[t:=t+1]}if k>78else[y|(y and e),2*0**(h:=len(y))+(min(s:={*map(len,sum(i,[]))}-{0})==h)*8+h//max(s)][k<1]for y,e in zip(x,x[:1]+x)]for x in zip(*i[::-1])],k-1)
