def p(g):
 B=len(g[a:=0]);F=sum(g,[]);i=9;Y=F.index(5)-~B
 while i:
  if{*g[a//B]}-{0,5}and{*F[a%B::B]}-{0,5}:i-=1;g[Y//B-i//3][Y%B-i%3]=F[a]
  a+=1
 return g

##

def p(g):
 r,c=[min(i for i,r in enumerate(k)if{*r}-{0,5})for k in(g,zip(*g))];I=sum(g,[]).index(5);W=len(g[0])
 for i in 0,1,2:g[I//W-1+i][I%W-1:I%W+2]=g[r+i][c:c+3]
 return g
