# att (126 bytes, gold)
p=lambda a,n=-3:n*a or p([[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))],n+1)

### joking+mwi (tied, 126 bytes)
p=lambda a,n=-3:n*a or p([[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))],n+1)
