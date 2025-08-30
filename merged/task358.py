# combined (97 vs 105 bytes for gold)
p=lambda i,k=39:-k*i or[[*map(max,x,x[6-13//len({*x,0}):]+(0,0)*9)]for x in zip(*p(i,k-1)[::-1])]

### att (105 bytes)
p=lambda a:[*map(f:=lambda*b:1<(n:=len({*b})-1)and[max(b[i%n::n])for i in range(len(b))]or b,*map(f,*a))]
