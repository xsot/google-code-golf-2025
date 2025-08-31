# att (61 vs 57 bytes for gold)
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]

### ovs (79 bytes)
E=enumerate
p=lambda g:[[min(i,j,v*99)%2*4or v for j,v in E(r)]for i,r in E(g)]
