# joking (173 bytes, gold)
p=lambda x,k=79,v=2:-k*x or p([(a:=1)*[(k>1and a|(b or(v:=v*2))or[b//max(f:=sum(x,[]))+min({*f}-{2})//b*8,f.count(b)+2][k],a:=b)[b==2]for b in r]for*r,in zip(*x[::-1])],k-1)

### ovs (179 bytes)
p=lambda x,k=79,v=2:-k*x or p([[(k>1and a|(b or(v:=v*2))or[b==max(f:=sum(x,[]))or(b==min({*f}-{2}))*8,f.count(b)+2][k],b)[b==2]for a,b in zip([0]+r,r)]for*r,in zip(*x[::-1])],k-1)

### combined (199 bytes)
p=lambda i,k=79,t=0:-k*i or p([[{*0**y*[t:=t+1]}if k>78else[y|(y and e),2*0**(h:=len(y))+(min(s:={*map(len,sum(i,[]))}-{0})==h)*8+h//max(s)][k<1]for y,e in zip(x,x[:1]+x)]for x in zip(*i[::-1])],k-1)
