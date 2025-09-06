def p(g):
 for E in range(8):
  I=[]
  for A,r in enumerate(g):
   for B,F in enumerate(r):
    G={(A,B)}
    for D in I[:F*5]:
     if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
    I+=[G][:F]
  for G in I:
   for A,B in G:
    for E in range(8):
     for F in range(8):
      if{(A-F,B-~E),(A-~F,B-E)}&{*G}:g[A-F][B-E]|=len({*str([x[B:B+2]for x in g[A:A+2]])})//8*g[A][B]
  *g,=map(list,zip(*g[::-1]))
 return g