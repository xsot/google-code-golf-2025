p=lambda x,k=7,v=2:-k*x or p([[a:=2*(b==2)or(k>1)*(a|(b or(v:=v*2)))or[b//max(f:=sum(x,[]))+min({*f}-{2})//b*8,f.count(b)+2][k]for b in[2]+r][:0:-1]for*r,in zip(*x)],k-1)

##
p=lambda x,k=79,v=2:-k*x or p([(a:=1)*[(k>1and a|(b or(v:=v*2))or[b//max(f:=sum(x,[]))+min({*f}-{2})//b*8,f.count(b)+2][k],a:=b)[b==2]for b in r]for*r,in zip(*x[::-1])],k-1)
p=lambda x,k=7,v=2:-k*x or p([(a:=1)*[a:=(k>1and a|(b or(v:=v*2))or[b//max(f:=sum(x,[]))+min({*f}-{2})//b*8,f.count(b)+2][k],b)[b==2]for b in r]for*r,in zip(*x[::-1])],k-1)