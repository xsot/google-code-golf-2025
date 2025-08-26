p=lambda m:[[min({*r[i:i+3]}-{5})for i in[0,3,6]]for r in m[::3]]

### ovs (tied, {ovs_score} bytes)
p=lambda g:[[sum({*r[j:j+3]}-{5})for j in(0,3,6)]for r in g[::3]]
