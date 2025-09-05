# combined (94 vs 93 bytes for gold)
def p(g):A=len(g);B=range(2,A-2);return[[g[C][B]%7*g[0-C*2//A][0-B*2//A]for B in B]for C in B]
