# combined (40 vs 39 bytes for gold)
p=lambda i:[[0**i[0][0]+0**i[0][2]*3^2]]

### ovs (43 bytes)
p=lambda g:[[5^(g[0][0]>0)-3*~(g[0][2]>0)]]

### xsot (46 bytes)
p=lambda m:[[hash((*map(bool,m[0]),))%1653%7]]
###
p=lambda m:[[hash((*map(bool,m[0]),))%1653%7]]
p=lambda m:[[hash((*(v>0for v in m[0]),))%1653%7]]
p=lambda m:[[hash(tuple(v>0for v in m[0]))%1653%7]]

a=[(1,hash((1,1,0))),
   (2,hash((1,0,1))),
   (3,hash((0,1,1))),
   (6,hash((0,1,0)))]
for i in range(1,100000):
    for j in range(1,10000):
        if all(v==k*i%j%7 for v,k in a):
            print(i,j); 1//0
