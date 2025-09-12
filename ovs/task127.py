p=lambda a,q=3:a*0==0and 5+a%5or a[1:]and[p(a[1])]*q+p(a[2:],4-q)

##

p=eval('lambda a:[[sum(b"%r0"%a)%5+5'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)
