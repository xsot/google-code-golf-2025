# ovs (63 vs 61 bytes for gold)
p=lambda a:[b[::(n:=~a.index(min(a,key=set)))]for b in a][::-n]

### joking (64 bytes)
p=lambda a,n=1:[b[::~n]for b in(a[n]!=a[0])*a][::1+n]or p(a,n+1)

### att (65 bytes)
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)

### combined (65 bytes)
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)
