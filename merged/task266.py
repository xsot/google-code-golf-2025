# ovs (99 vs 88 bytes for gold)
p=lambda g:[([0,0,0,r%9,0,r%8]*2)[4-max(g).index(2):][:5]for r in b'HfHGH'[2-g.index(max(g)):][:3]]

### joking (102 bytes)
p=lambda g:[([0,0,0,r%9,0,r//9-4]*2)[4-max(g).index(2):][:5]for r in b'$]$k$'[2-g.index(max(g)):][:3]]

### combined (103 bytes)
p=lambda g:[([0,0,0,r%9,0,r//9]*2)[4-max(g).index(2):][:5]for r in b'\09\0G\0'[2-g.index(max(g)):][:3]]
