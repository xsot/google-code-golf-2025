# att (65 bytes, gold)
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]

### joking+mwi (tied, 65 bytes)
p=lambda g:[[max({*A[B:B+3]}-{5})for B in[0,3,6]]for A in g[::3]]

### ovs (tied, 65 bytes)
p=lambda g:[[sum({*r[j:j+3]}-{5})for j in(0,3,6)]for r in g[::3]]

### xsot (tied, 65 bytes)
p=lambda m:[[min({*r[i:i+3]}-{5})for i in[0,3,6]]for r in m[::3]]
