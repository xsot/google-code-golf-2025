def p(j,r=range(21)):
 n=[n+1for n in r if all(len({*j[0][b::n+1],0})<3for b in r)][0]
 for x in r:
  for y in r:j[x%n][y%n]|=j[x][y]
 return[[j[x%n][y%n]for y in r]for x in r]