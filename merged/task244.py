# joking (64 vs 63 bytes for gold)
p=lambda a,n=1:[b[::~n]for b in(a[n]!=a[0])*a][::1+n]or p(a,n+1)

### att (65 bytes)
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)

### combined (65 bytes)
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)

### ovs (70 bytes)
p=lambda g:[r[::(w:=~[len({*r})for r in g].index(1))]for r in g][::-w]
