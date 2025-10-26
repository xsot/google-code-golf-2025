# att (51 bytes, gold)
p=lambda g,v=0:g*0!=0and[*map(p,g,b'\n'*7)]or-g%v

### joking (53 bytes)
p=lambda g,v=0:g*0!=0and[*map(p,g,b''*7)]or g*v//4

### ovs (57 bytes)
p=lambda g:[[j*v//4for j,v in zip(b''*7,r)]for r in g]

### combined (58 bytes)
p=lambda i:[[8%~y&6-b%3for b,y in enumerate(x)]for x in i]
