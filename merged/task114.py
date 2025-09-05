# ovs (65 vs 2500 bytes for gold)
p=lambda g:[[0,*g[0],0],*[r[:1]+r+r[-1:]for r in g],[0,*g[-1],0]]

### combined (tied, 65 bytes)
p=lambda i:[[0,*i[0],0],*[x[:1]+x+x[-1:]for x in i],[0,*i[-1],0]]
