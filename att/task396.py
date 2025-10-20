p=lambda m,n=266,f=0:[[sum({*e*sum(m,[-f])})for e in s]for r in m if(f:=((X:=n>>5)*[a:=(r*3)[x:=n%32]]in(s:=r[x:x+X],[f]*X))*a)]or p(m,n-1)
##
p=lambda m,w=171,f=0:[[sum({*e*sum(m,[-f])})for e in s]for r in m if(f:=(w//20*[a:=(r*2)[w%20]]in(s:=r[w%20:w%19],w//20*[f]))*a)]or p(m,w-1)