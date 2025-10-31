# joking (130 vs 115 bytes for gold)
p=lambda i:[i:=[*zip(*map(max,i,(i*2)[j*2::-1]+i[::-1]))]for j in b'	'*2if[x.count(max(i[j]))for x in i[j-1:j+2]]==[2,1,2]][1]

### ovs (134 bytes)
p=lambda i:[i:=[*zip(*map(max,i,(i*2)[j*2::-1]+i[::-1]))]for j in b'	'*2if[x.count(max(i[j]))for x in i[j-2:j+3]]==[0,2,1,2,0]][1]

##

p=lambda i:[i:=[*zip(*map(max,i,(i*2)[w.index(1)*2::-1]+i[::-1]))]for n in range(20)if[*filter(abs,w:=[x.count(n%10)for x in i])]==[2,1,2]][1]

### combined (172 bytes)
p=lambda i,k=1:-k*i or p([[*map(max,x,[*x,*(s:=sum(i,[]))][s.index(max(s,key=lambda n:[x.count(n)for x in i if n in x]==[2,1,2]))//len(i)*2+2::-1]+s)]for x in zip(*i)],k-1)
