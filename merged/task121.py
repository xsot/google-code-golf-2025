# ovs (88 vs 85 bytes for gold)
p=lambda g:exec("g[:]=map(list,zip(*g[(8in g[-2])-2::-1]));"*40+"g[1][1]=max(g[0])")or g

##
p=lambda g,k=39:[[sum({*g[0]*v})for v in r]for r in-k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k-1)
p=lambda g,k=39:[[sum({*g[0]*v})for v in r]for r in-k*g]or p([*zip(*g[1-(8in g[1]):2+k|1])],k-1)
def p(g):x=sum(g,[]).index(8)-14;C=[g[x%13:][:3]for g in g[x//13:][:3]];C[1][1]=max(C[0]);return C

### mwi (90 bytes)
p=lambda g:exec("g[:]=*map(list,zip(*g[(8in g[-2])-2::-1])),;"*40+"g[1][1]=max(g[0])")or g
##
def p(g):exec("g[:]=*map(list,zip(*g[(8in g[-2])-2::-1])),;"*40);g[1][1]=max(g[0]);return g

### joking (92 bytes)
def p(g):
 for _ in g*4:*g,=map(list,zip(*g[(8in g[-2])-2::-1]))
 g[1][1]=max(g[0]);return g

##
def p(g):
 for _ in g*4:g=[b for*b,in zip(*g[(8in g[-2])-2::-1])]
 g[1][1]=max(g[0]);return g

p=lambda g,k=39:-k*g or p([[max(g[0])*(k*9<x)or x for x in b]for*b,in zip(*g[(8in g[-2])-2::-1])],k-1)
def p(g,k=39):g=-k*g or p([b for*b,in zip(*g[(8in g[-2])-2::-1])],k-1);g[1][1]=max(g[0]);return g
def p(g,k=39):g=-k*g or p([*map(list,zip(*g[(8in g[-2])-2::-1]))],k-1);g[1][1]=max(g[0]);return g
def p(g,k=40):k and(g:=p([*map(list,zip(*g[(8in g[-2])-2::-1]))],k-1));g[1][1]=max(g[0]);return g

### combined (96 bytes)
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)
