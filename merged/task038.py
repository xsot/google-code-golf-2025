# combined (52 vs 51 bytes for gold)
p=lambda g:[(str(g).count('1, 1')//2*[1]+[0]*5)[:5]]

### ovs (tied, 52 bytes)
p=lambda g:[(str(g).count('1, 1')//2*[1]+[0]*5)[:5]]
