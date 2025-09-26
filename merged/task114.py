# ovs (64 bytes, gold)
*R,p=0,lambda g:[R+g[0]+R,*[r[:1]+r+r[-1:]for r in g],R+g[-1]+R]

### combined (65 bytes)
p=lambda i:[[0,*i[0],0],*[x[:1]+x+x[-1:]for x in i],[0,*i[-1],0]]
