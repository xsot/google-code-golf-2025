p=lambda g,R=[]:g and p(g[:-1],w:=[g[-1][x]or(1in R[x:]>[1])*max(sum(g[-2:],R))for x in range(10)])+[w]

##
p=lambda g:[g:=[[r[x]or(1in g[0][x:]>[1])*max(g[8]+r+g[0])for x in range(10)]]+g[:9]for r in g[::-1]][9]
