p=lambda g,k=39:[[sum({*g[0]*v})for v in r]for r in-k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k-1)

##

p=lambda g,k=39:[[sum({*g[0]*v})for v in r]for r in-k*g]or p([*zip(*g[1-(8in g[1]):2+k|1])],k-1)
def p(g):x=sum(g,[]).index(8)-14;C=[g[x%13:][:3]for g in g[x//13:][:3]];C[1][1]=max(C[0]);return C
