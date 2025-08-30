# att (57 vs 52 bytes for gold)
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(4)]for b in a]

### combined (tied, 57 bytes)
p=lambda i:[[~y+t&2for y,t in zip(x,i.pop(4))]for x in i]

### ovs (60 bytes)
p=lambda g:[[V+~v&2for v,V in zip(*r)]for r in zip(g,g[4:])]
