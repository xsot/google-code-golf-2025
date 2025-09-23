p=lambda g:[[v+3-3*(c>[-v]*99<r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]

## recursive approach
p=lambda g,w=[],*s:g+3-3*(w>[-g]*99<[*s])if s else[*map(p,g,[g[1:-1]]*99,*w)]