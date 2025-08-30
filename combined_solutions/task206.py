def p(g):
 e=enumerate;(y,x),(Y,X)=[min((y,x)for y,r in e(g)for x,c in e(zip(*g))if{*r}&k and{*c}&k)for k in({5},{*b"	"})]
 for n in[0,1,2]:g[y+n-1][x-1:x+2]=g[Y+n][X:X+3]
 return g