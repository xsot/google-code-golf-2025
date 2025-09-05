# mwi (78 vs 74 bytes for gold)
p=lambda g:[[v or 3-3*any(min(c,r[1:-1]))for _,*c,_,v in zip(*g,r)]for r in g]

### xsot (tied, 78 bytes)
p=lambda g:[[v or 3-3*any(c)*any(r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]

### ovs (79 bytes)
p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]

### combined (79 bytes)
p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]
