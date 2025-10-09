def p(g):
 W=len(g[0]);s=sum(G:=g,[]).index(5)+~W
 for g[s//W][s%W:s%W+3]in[G:=[r for*r,in zip(*G)if{*r}-{0,5}]for _ in g][1]:s+=W
 return g

##

def p(g):
 r,c=[min(i for i,r in enumerate(k)if{*r}-{0,5})for k in(g,zip(*g))];I=sum(g,[]).index(5);W=len(g[0])
 for i in 0,1,2:g[I//W-1+i][I%W-1:I%W+2]=g[r+i][c:c+3]
 return g
