p=lambda a:[p(b)for*b,in map(zip,a,a[4:])]or max(sum(a+a,())[1:],key=bool)

##
p=lambda a,*b:a*0!=0and[*map(p,a,a[4:],*b,[*b,a][0][4:])]or max(*b,a,key=bool)