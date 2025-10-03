p=lambda i,k=39:-k*i or[[*map(max,x,-14//len({*x,0})%7*[0]+x)]for*x,in zip(*p(i,k-1)[::-1])]

##
p=lambda a:[*map(f:=lambda*b:1<(n:=len({*b})-1)and[max(b[i%n::n])for i in range(len(b))]or b,*map(f,*a))]