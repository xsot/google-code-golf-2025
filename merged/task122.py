# joking+mwi (94 vs 88 bytes for gold)
p=lambda i:sum(map(max,i))<8and[[x[0]%2*3,x[1]%2*3,*x[:-2]]for x in i]or[*zip(*p([*zip(*i)]))]

### ovs (102 bytes)
p=lambda g:[[v%2*v|o[sum(3in r for r in g)<2]%3for*o,v in zip(i,[0,0]+r,r)]for i,r in zip(g[-2:]+g,g)]
