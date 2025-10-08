def p(g):
 R=F=sum(g,[])
 while C:=max(F):
  o=F.index(C)-2;N={d for d in range(65)if d%20<6!=F[d+o:]>=[C]}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g

## 183, doesn't work, execs hate comprehensions
def p(g):R=F=sum(g,[]);exec("o=F.index(C:=max(F))-2;N={d for d in range(65)if d%20<6!=F[d+o:]>=[C]}\nfor i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W\nif C>1:R,W=N,C\n"*99);return g

## thoughts:
# only the training/test cases have more than one grey box, and the relevant one is always the bottom right one
# we could also get the replacement sprite by rindex(5)
# the replacement colour is always red/green (2/3)
# real boxes are 7x7
# there are only 10 possible shapes (which is probably too annoying to hardcode)