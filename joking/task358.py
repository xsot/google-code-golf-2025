p=lambda i,k=23:-k*i or[[*map(max,x,84//len({*x,0})%6*[0]+x)]for*x,in zip(*p(i,k-1)[::-1])]

##
p=lambda i,k=39:-k*i or[[*map(max,x,-14//len({*x,0})%7*(0,)+x)]for x in zip(*p(i,k-1)[::-1])]