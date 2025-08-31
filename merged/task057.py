# att (49 bytes, gold)
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]

### combined (tied, 49 bytes)
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]

### ovs (64 bytes)
p=lambda g,k=-1:k*g[:3]or p([r for*r,in zip(*g*2)if any(r)],k+1)
