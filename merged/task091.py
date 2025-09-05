# att (63 vs 2500 bytes for gold)
p=lambda a,n=46:a*~n or p([*zip(*a[(5in a[n%2-2])-2::-1])],n-1)

### combined (tied, 63 bytes)
p=lambda a,n=46:a*~n or p([*zip(*a[(5in a[n%2-2])-2::-1])],n-1)
