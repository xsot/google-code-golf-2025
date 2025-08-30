# ovs (224 vs 139 bytes for gold)
def p(g):
 o=eval(str(g));R={*range(6)}
 for i in R:
  for j in R:
   for S in b' *#-':
    for A in({i+(d:=S%5-1),j+(D:=S%3-1)}<R!=0<o[i+d][j+D])*b"*/&+":
     if{b:=A%5*d+i,B:=A%4*D+j}<R:g[b][B]=g[b][B]or o[i][j]
 return g
