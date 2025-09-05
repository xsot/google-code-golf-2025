# ovs (136 bytes, gold)
def p(i):z,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]

### combined (169 bytes)
def p(i):s,b=sorted({*sum(i,[])}-{0},key=lambda n:(f"{n}, "*3in str(i))*-n^7);return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]
