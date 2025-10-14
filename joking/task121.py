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