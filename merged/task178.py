# att (49 vs 47 bytes for gold)
p=lambda a:a*-1*-1or[p(b)for b in a if a!=(a:=b)]

### combined (tied, 49 bytes)
p=lambda a:a*-1*-1or[p(b)for b in a if a!=(a:=b)]

### ovs (62 bytes)
p=lambda g,k=-1:k*g or p([r for*r,in zip(*g)if g!=(g:=r)],k+1)
