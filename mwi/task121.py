p=lambda g:exec("g[:]=*map(list,zip(*g[(8in g[-2])-2::-1])),;"*96+"g[1][1]=max(g[0])")or g
##
def p(g):exec("g[:]=*map(list,zip(*g[(8in g[-2])-2::-1])),;"*96);g[1][1]=max(g[0]);return g