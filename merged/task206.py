# ovs (140 bytes, gold)
def p(g):
 W=len(g[0]);s=sum(G:=g,[]).index(5)+~W
 for g[s//W][s%W:s%W+3]in[G:=[r for*r,in zip(*G)if{*r}-{0,5}]for _ in g][1]:s+=W
 return g

##

def p(g):
 r,c=[min(i for i,r in enumerate(k)if{*r}-{0,5})for k in(g,zip(*g))];I=sum(g,[]).index(5);W=len(g[0])
 for i in 0,1,2:g[I//W-1+i][I%W-1:I%W+2]=g[r+i][c:c+3]
 return g

### joking (141 bytes)
# 141
def p(g):
 W=len(g[0]);s=sum(G:=g,[]).index(5)+~W
 for _ in'  ':G=[r for*r,in zip(*G)if{*r}-{0,5}]
 for g[s//W][s%W:s%W+3]in G:s+=W
 return g

##
def p(g,E=enumerate):
 r,c=map(min,*[(a,b)for a,x in E(g)for b,y in E(x)if y%5or y>0==(s:=a,t:=b)])
 for i in-1,0,1:g[s+i][t-1:t+2]=g[r-~i][c:c+3]
 return g

### combined (176 bytes)
def p(g):
 r,c=[min(i for i,r in enumerate(k)if{*r}-{0,5})for k in(g,zip(*g))];I=sum(g,[]).index(5);W=len(g[0])
 for i in 0,1,2:g[I//W-1+i][I%W-1:I%W+2]=g[r+i][c:c+3]
 return g
