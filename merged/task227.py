# joking (52 bytes, gold)
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[4:]+n)]or~a+n&2

### att (55 bytes)
p=lambda a:[[~b.pop(0)+c&2for c in a.pop(4)]for b in a]

### combined (57 bytes)
p=lambda i:[[~y+t&2for y,t in zip(x,i.pop(4))]for x in i]

### ovs (60 bytes)
p=lambda g:[[V+~v&2for v,V in zip(*r)]for r in zip(g,g[4:])]
