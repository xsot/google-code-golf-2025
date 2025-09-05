# combined (62 vs 2500 bytes for gold)
p=lambda g:[[g[1][x]*sum(g[2][x:x+3])%13^8]*3for x in[1,6,11]]

### ovs (66 bytes)
p=lambda g:[[1-g[2][s+1]*2-g[1][s]&g[3][s+2]+6]*3for s in(0,5,10)]

### xsot (69 bytes)
p=lambda m:[3*[(541^sum(m[2][i:i+3]+m[3][i:i+3]))%9]for i in[0,5,10]]
# p=lambda m:[3*[(541^sum(m[2][i*5:][:3]+m[3][i*5:][:3]))%9]for i in[0,1,2]]

# 30: 2
# 20: 8
# 25: 3
# 10: 4
