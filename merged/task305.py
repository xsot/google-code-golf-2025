# ovs (74 vs 62 bytes for gold)
p=lambda g:[[max(r[j%(n:=len({*r}-{0}))::n])for j in range(16)]for r in g]
