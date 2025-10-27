p=lambda a,i=2:[p(b,4)for*b,in map(zip,a,a[i:])]or max(max(a))

##
p=lambda a:[*map(f:=lambda*b:[*map(max,b,b[-3:])],*map(f,*a))]
p=lambda a:[a:=[*zip(*map(map,[max]*3,a,a[-3:]))]for _ in a][1]
p=lambda a,*n:[[*map(max,b,b[-3:])]for b in zip(*n or p(a,*a))]
p=eval('lambda a:[[max(max(a))'+'for*a,in map(zip,a,a[-3:])]'*2)