# ovs (104 bytes, gold)
p=lambda a,n=1:[[d&e for d in b for e in c]for b in a for c in-n*a]or p([*filter(any,zip(*a[::3]))],n-1)

### att (105 bytes)
p=lambda a,n=-1:n*[[d&e for d in b for e in c]for b in a for c in a]or p([*filter(any,zip(*a[::3]))],n+1)

### combined (105 bytes)
p=lambda a,n=-1:n*[[d&e for d in b for e in c]for b in a for c in a]or p([*filter(any,zip(*a[::3]))],n+1)
