#alt
def p(i):a,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a-1]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for x in i if(a:=a+1)]