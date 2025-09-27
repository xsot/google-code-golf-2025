p=lambda a,n=1:[[d&e for d in b for e in c]for b in a for c in-n*a]or p([*filter(any,zip(*a[::3]))],n-1)
