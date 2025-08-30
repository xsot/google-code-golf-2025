# joking+mwi (199 vs 152 bytes for gold)
p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else(y|(y-{0}and e-{0}or{0}))if k else sorted({*map(len,sum(i,[]))}).index(len(y))**2%12%7for y,e in zip(x,[{*()},*x])]for x in zip(*i[::-1])],k-1)
