# joking+mwi (79 vs 72 bytes for gold)
def p(g,A=0,C=-1):
 for x in g[::-1]:x[A]=1;C*=-(A%~-len(x)<1)|1;A+=C
 return g
