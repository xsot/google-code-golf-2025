# joking (94 bytes, gold)
# alt
def p(g):A=len(g);B=range(2,A-2);return[[g[g[C][B]%5-3-C*2//A][0-B*2//A]for B in B]for C in B]

### combined (tied, 94 bytes)
def p(g):A=len(g);B=range(2,A-2);return[[g[C][B]%7*g[0-C*2//A][0-B*2//A]for B in B]for C in B]
