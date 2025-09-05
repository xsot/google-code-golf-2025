# mwi (51 vs 2500 bytes for gold)
p=lambda g:[(str(g).count('1, 1')*[1]+[0]*9)[:9:2]]

### ovs (52 bytes)
p=lambda g:[(str(g).count('1, 1')//2*[1]+[0]*5)[:5]]

### combined (52 bytes)
p=lambda g:[(str(g).count('1, 1')//2*[1]+[0]*5)[:5]]
