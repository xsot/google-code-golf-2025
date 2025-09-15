# xsot (77 vs 72 bytes for gold)
def p(m,c=0,d=1):
 for r in m[::-1]:r[c]=1;c+=d;c%~-len(r)or(d:=-d)
 return m

### combined (79 bytes)
def p(g,A=0,C=-1):
 for x in g[::-1]:x[A]=1;C*=-(A%~-len(x)<1)|1;A+=C
 return g
