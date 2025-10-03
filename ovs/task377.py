p=lambda g,k=-1:g*k or p([y for*y,in zip(*g)if g!=(g:=y)],k+1)
##
p=lambda a,*w:a*-1*-1or[p(b[0],*a)for b in zip(a,*w)if w!=(w:=b)]
