# mwi (167 vs 139 bytes for gold)
# slight modification of ovs's solution to remove the need for def.
#  takes 5 seconds because of assignment of `C` being moved into the loop
p=lambda g,Q=range(10):[[g[i][j]|any(all(((g+g[:1]*3)[i+y*[(C:=sum(b'%r'%g)//38%4),-C][S%2]]+g[0])[j+C*[3-y,y-3][S>5]]for y in(1,2))for S in Q)*8for j in Q]for i in Q]

## ovs's version
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]

### ovs (169 bytes)
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]

### combined (169 bytes)
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]
