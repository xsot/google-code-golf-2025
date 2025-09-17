# ovs (81 bytes, gold)
p=lambda a:7in map(sum,a)and a[-2:][::len(a)%-2|1]+a[:-2]or[*zip(*p([*zip(*a)]))]

##

p=lambda g:[[v%2*v|o[sum(3in r for r in g)<2]%3for*o,v in zip(i,[0,0]+r,r)]for i,r in zip(g[-2:]+g,g)]

### att (82 bytes)
p=lambda a:7in map(sum,a)and a[-2:][::(-1)**len(a)]+a[:-2]or[*zip(*p([*zip(*a)]))]

### combined (94 bytes)
p=lambda i:sum(map(max,i))<8and[[x[0]%2*3,x[1]%2*3,*x[:-2]]for x in i]or[*zip(*p([*zip(*i)]))]
