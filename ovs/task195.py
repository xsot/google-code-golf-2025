p=lambda a,n=1:[[y&sum(a*3,())[n:=n+3]for y in x]for x in-n*a]or p([*filter(any,zip(*a))],n-1)
