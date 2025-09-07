# mwi (144 vs 134 bytes for gold)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a:[a:=[b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]]for _ in a][3]

### att (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)

### combined (145 bytes)
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)
