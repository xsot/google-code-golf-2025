# joking+mwi (62 bytes, gold)
p=lambda g:[(sorted({*g[0]}-{0})*9)[y:y+16]for y in range(16)]

### ovs (74 bytes)
p=lambda g:[[max(r[j%(n:=len({*r}-{0}))::n])for j in range(16)]for r in g]
