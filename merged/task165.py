# att (130 bytes, gold)
def p(i):_,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(b in t[[*t[:a]+i,s].index(s):])*b for*t,in zip(*i)]for a in range(20)]

### joking (136 bytes)
#alt
def p(i):a,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a-1]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for x in i if(a:=a+1)]

### ovs (136 bytes)
def p(i):z,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]

### combined (169 bytes)
def p(i):s,b=sorted({*sum(i,[])}-{0},key=lambda n:(f"{n}, "*3in str(i))*-n^7);return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]
