p=lambda g:[r[::(w:=~[len({*r})for r in g].index(1))]for r in g][::-w]

### att (75 bytes)
p=lambda a,*n:[*zip(*n or p(a,*a)[::-1])][::1+[b!=a[0]for b in a].index(1)]
