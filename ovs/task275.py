p=lambda i:"8"in"%s"%i[(u:=len(i[0])):]and[[t*y/8for t in s for y in x]for s in i[:u]for x in i[u:]]or[*zip(*p([*zip(*i[::-1])]))][::-1]

##

p=lambda g,k=-3:g*k or p([h:=[*zip(*g[(w:=len(g))::-1])],[[v*t//8for v in c for t in r]for c in h[:w]for r in h[w:]]]['8'in str(h[w:])],k+1)
