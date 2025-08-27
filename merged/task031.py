p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)))]

### xsot (52 bytes)
p=lambda m,i=1:-i*m or p([*filter(sum,zip(*m))],i-1)
###
p=lambda m,i=1:-i*m or p([*filter(sum,zip(*m))],i-1)
p=lambda m,i=1:-i*m or[[*l]for l in zip(*p(m,i-1))if sum(l)]
p=lambda m,i=2:i and[[*l]for l in zip(*p(m,i-1))if sum(l)]or m
p=lambda m,i=2:i and p([[*l]for l in zip(*m)if sum(l)],i-1)or m
p=lambda m,i=0:m*(i>1)or p([[*l]for l in zip(*m)if sum(l)],i+1)
p=lambda m,i=0:m*(i>1)or p([*map(list,filter(sum,zip(*m)))],i+1)
p=lambda m,i=0:m*(i>1)or p([*map(list,zip(*filter(sum,m)))],i+1)

### ovs (59 bytes)
p=lambda g,k=-1:k*g or p([r for*r,in zip(*g)if any(r)],k+1)
