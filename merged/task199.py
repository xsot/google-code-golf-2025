# joking (100 vs 84 bytes for gold)
def p(g):r=range(len(g));return[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B in r]for A in r]

### combined (102 bytes)
p=lambda g,E=enumerate:[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B,_ in E(x)]for A,x in E(g)]
