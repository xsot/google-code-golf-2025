# joking (75 bytes, gold)
p=lambda g:[[v+3-3*(c>[-v]*99<r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]

## recursive approach
p=lambda g,w=[],*s:g+3-3*(w>[-g]*99<[*s])if s else[*map(p,g,[g[1:-1]]*99,*w)]

### ovs (tied, 75 bytes)
p=lambda g,w=[],*s:g|3>>g+sum(w)*sum(s)if s else[*map(p,g,[g[1:-1]]*99,*w)]

##
p=lambda g:[[v or(c>[0]*99<r[1:-1])*3^3for _,*c,_,v in zip(*g,r)]for r in g]
p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]

### att (77 bytes)
p=lambda g:[[v or 3^3*(c>[0]*99<r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]

### mwi (78 bytes)
p=lambda g:[[v or 3-3*any(min(c,r[1:-1]))for _,*c,_,v in zip(*g,r)]for r in g]

### xsot (78 bytes)
p=lambda g:[[v or 3-3*any(c)*any(r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]

### combined (79 bytes)
p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]
