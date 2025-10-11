p=lambda a:[*zip(*[(max(sum(a,a)[x::3])for x in[7,8,9]*17)]*7)]

##
p=lambda a:[[max(sum(a:=a[1:3]+a,r)[9::3])for _ in r]for r in a]