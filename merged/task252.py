# joking (57 bytes, gold)
p=lambda a:[(i:=1)*[(i:=-i)*4%(c+4)for c in b]for b in a]

## alts
p=lambda a:[(i:=4)and[(i:=-i)%(c+4)for c in b]for b in a]
p=lambda a:[[(i:=-i)%(c+4)for c in b]for b in a if[i:=4]]

#and regex, for fun
import re;p=lambda i:eval(re.sub("(\d, .)",r"\1and 4",str(i)))

### att (61 bytes)
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]

### combined (61 bytes)
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]

### ovs (79 bytes)
E=enumerate
p=lambda g:[[min(i,j,v*99)%2*4or v for j,v in E(r)]for i,r in E(g)]
