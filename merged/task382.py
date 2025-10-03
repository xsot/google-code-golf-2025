# joking (124 bytes, gold)
p=lambda i,k=-3:k*i or p([*zip(w:=i.pop(),*[[*map(max,r,w:=r*('8'in'%s'%i)+[0,*w,0][r[-1]or[1]>r:])]for*r,in i[::-1]])],k+1)

### ovs (125 bytes)
p=lambda i,k=-3:k*i or p([*zip(w:=i.pop(0),*[[*map(max,r,w:=r*('8'in'%s'%i)+[0,*w,0][r[-1]or[1]>r:])]for*r,in i])][::-1],k+1)

### mwi (144 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a:[a:=[b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]]for _ in a][3]

### att (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)

### combined (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)
