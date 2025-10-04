p=lambda a:[[min(b:=sum(a[1:-1],a[3]),key=b.count)]]

##
p=lambda a:[[min(b:=sum(a+a[1:8],a[2]),key=b.count)]]