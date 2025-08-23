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