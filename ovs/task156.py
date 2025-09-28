p=lambda i,r=range(10),S=sum:[[i[a][b]-S(S(t[b-1:b+2])for t in i[a-1:a+2])//36*(S(t:=[*map(S,i)])//S(t[:t.index(0,1)]*2)+2^a//5)for b in r]for a in r]

##

p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else y|(y-{0}and e-{0}or{0})if k else sum(x<len(y)for x in{*map(len,sum(i,[]))})**2%12%7for y,e in zip(x,[{0}]+x)]for*x,in zip(*i[::-1])],k-1)
