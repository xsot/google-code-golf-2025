# ovs (154 vs 148 bytes for gold)
p=lambda i:[i:=[*zip(*map(max,i,(i*2)[[w.index(1)for n in range(10)if[*filter(abs,w:=[x.count(n)for x in i])]==[2,1,2]][0]*2::-1]+i[:1]*9))]for _ in i][1]

### combined (172 bytes)
p=lambda i,k=1:-k*i or p([[*map(max,x,[*x,*(s:=sum(i,[]))][s.index(max(s,key=lambda n:[x.count(n)for x in i if n in x]==[2,1,2]))//len(i)*2+2::-1]+s)]for x in zip(*i)],k-1)
