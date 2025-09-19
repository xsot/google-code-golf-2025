p=lambda m,X=8,f=0:[[sum({*e*sum(m,[-f])})for e in r[x:x+X]]for x in range(len(m[0]))for r in m+[[0]*99]if(f:=r[x]*(X*[r[x]]in(r[x:x+X],[f]*X)))]or p(m,X-1)
