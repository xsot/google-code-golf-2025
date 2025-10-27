# att (84 vs 81 bytes for gold)
p=lambda g:-~(i:=g.index(m:=max(g)))*[([4,0]*15)[m.index(max(m)):][:len(g)]]+g[i:-1]

### ovs (87 bytes)
p=lambda g:[([4,0]*8)[(m:=max(g)).index(max(m))%2:][:len(g)]]*-~(i:=g.index(m))+g[i:-1]

### joking (100 bytes)
def p(g):r=range(len(g));return[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B in r]for A in r]

### combined (102 bytes)
p=lambda g,E=enumerate:[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B,_ in E(x)]for A,x in E(g)]
