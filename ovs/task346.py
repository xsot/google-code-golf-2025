S=lambda g:zip(g[1:],g[2:],g)
p=lambda g:[[v for r in S(g)for(v,*q),a,b in zip(*map(S,r))if not{0,v}&{*q,*a+b}]]