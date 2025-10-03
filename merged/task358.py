# att (92 bytes, gold)
p=lambda i,k=39:-k*i or[[*map(max,x,-14//len({*x,0})%7*[0]+x)]for*x,in zip(*p(i,k-1)[::-1])]

##
p=lambda a:[*map(f:=lambda*b:1<(n:=len({*b})-1)and[max(b[i%n::n])for i in range(len(b))]or b,*map(f,*a))]

### joking (93 bytes)
p=lambda i,k=39:-k*i or[[*map(max,x,-14//len({*x,0})%7*(0,)+x)]for x in zip(*p(i,k-1)[::-1])]

### combined (97 bytes)
p=lambda i,k=39:-k*i or[[*map(max,x,x[6-13//len({*x,0}):]+(0,0)*9)]for x in zip(*p(i,k-1)[::-1])]
