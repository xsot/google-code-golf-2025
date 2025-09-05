def p(i):z,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]
