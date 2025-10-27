# att (117 vs 115 bytes for gold)
p=lambda g:g[(T:=[*zip(*[map(bool,sum(g,g*0))]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p((*zip(*g),)))]

### ovs (122 bytes)
p=lambda g:g[(T:=[*zip(*[(x>0for y in g for x in y)]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p([*zip(*g)]))]

### combined (122 bytes)
p=lambda g:g[(T:=[*zip(*[(x>0for y in g for x in y)]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p([*zip(*g)]))]
