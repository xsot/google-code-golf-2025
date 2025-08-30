# joking+mwi (74 vs 65 bytes for gold)
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]

### ovs (tied, 74 bytes)
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]
