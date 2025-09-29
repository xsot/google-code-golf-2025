p=lambda i,a=-38:[[v-(str(i)[(a:=a+3)::35][:3]=='444')*(sum(t:=[*map(sum,i)])//sum(t[:t.index(0,1)]*2)+2^a//126)for v in r]for r in i if[a:=a+2]]

##

p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else y|(y-{0}and e-{0}or{0})if k else sum(x<len(y)for x in{*map(len,sum(i,[]))})**2%12%7for y,e in zip(x,[{0}]+x)]for*x,in zip(*i[::-1])],k-1)
