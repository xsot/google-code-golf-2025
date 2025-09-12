p=lambda a:7in map(sum,a)and a[-2:][::len(a)%-2|1]+a[:-2]or[*zip(*p([*zip(*a)]))]

##

p=lambda g:[[v%2*v|o[sum(3in r for r in g)<2]%3for*o,v in zip(i,[0,0]+r,r)]for i,r in zip(g[-2:]+g,g)]
