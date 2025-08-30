def p(g,Q=80):
 for C in range(((D:={*g[A:=Q%9][(B:=Q//9):B+2],*g[A+1][B:B+2]})-{0,3}==D)*len(D)):g[A+2+C][B:B+2]=[3,3]
 return-~-Q*g or p(g,Q-1)