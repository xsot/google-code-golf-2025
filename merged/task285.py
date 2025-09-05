# ovs (309 (426 unzipped) vs 291 bytes for gold)
def p(g):
 for _ in range(8):
  I=[]
  for A,r in enumerate(g):
   for B,F in enumerate(r):
    G={(A,B)}
    for D in I[:F*5]:
     if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
    I+=[G][:F]
  for G in I:
   for C,D in G:
    for E in range(5):
     for F in range(5):
      if{*G}&{(C-F,D-~E),(C-~F,D-E)}:g[C-F][D-E]|=len({*str([x[D:D+2]for x in g[C:C+2]])})//8*g[C][D]
  *g,=map(list,zip(*g[::-1]))
 return g

### combined (317 (400 unzipped) bytes)
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
