# ovs (140 vs 137 bytes for gold)
p=lambda g,k=-3:g*k or p([h:=[*zip(*g[(w:=len(g))::-1])],[[v*t//8for v in c for t in r]for c in h[:w]for r in h[w:]]]['8'in str(h[w:])],k+1)
