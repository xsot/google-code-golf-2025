# joking (61 bytes, gold)
p=lambda g,r=5:[[x|~r*(r:=r-x)%6for x in s]*(r:=1)for s in g]

### ovs (74 bytes)
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]

### combined (74 bytes)
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]
