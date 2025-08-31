# combined (317 (400 unzipped) vs 306 bytes for gold)
def p(g,k=7):
 I=[]
 for A,r in enumerate(g):
  for B,F in enumerate(r):
   G={(A,B)}
   for D in(F>0)*I:
    if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
   I+=(F>0)*[G]
 for G in I:
  for C,D in G:
   for E in range(25):
    if{*G}&{(C-E%5,E//5-~D),(E%5-~C,D-E//5)}:g[C-E%5][D-E//5]|=len({*str([x[D:D+2]for x in g[C:C+2]])})//8*g[C][D]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
