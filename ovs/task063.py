p=lambda g:[[v or(c>[0]*99<r[1:-1])*3^3for _,*c,_,v in zip(*g,r)]for r in g]

##

p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]
