p=lambda m:[[max(max(m))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]
##
p=lambda m:[[max(sum(m,[]))*any(i)for i in zip(x,y,x[4:],y[4:])]for x,y in zip(m,m[2:])]