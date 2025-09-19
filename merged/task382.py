# ovs (137 vs 134 bytes for gold)
p=lambda i,k=-7:k*i or p([*zip(w:=i.pop(0),*[i,[[f]+(w:=[0,*w][f<1:])[1:]for f,*_ in i]][max(i)[0]and'8'not in'%s'%i])][::k%4<1or-1],k+1)

### mwi (144 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a:[a:=[b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]]for _ in a][3]

### att (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)

### combined (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)
