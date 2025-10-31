# joking (134 vs 132 bytes for gold)
p=lambda g,Q=range(10):[g:=[[g[j][~i]|g[j-C-C][~i+C]*g[j-C][~i+C+C]%~(i>C<j)%9for j in Q]for i in Q]for C in[sum(b'%r'%g)//38%4]*4][3]

### mwi (140 bytes)
# collapsed `all` into single check
def p(g,Q=range(10)):C=sum(b'%r'%g)//38%4;return[g:=[[g[j][~i]|8*((i>C<j)&g[j-C-C][~i+C]&g[j-C][~i+C+C])for j in Q]for i in Q]for _ in Q][3]

## same length using exec
exec(f"def p(g):C=sum(b'%r'%g)//38%4;return[g:=[[g[j][~i]|8*((i>C<j)&g[j-C-C][~i+C]&g[j-C][~i+C+C]){'for %s in range(10)]'*3%(*'ji_',)}[3]")

# improved oob check over previous version
def p(g,Q=range(10)):C=sum(b'%r'%g)//38%4;return[g:=[[g[j][~i]|8*all((i>y<j)&g[j-3*C+y][~i+y]for y in(C,2*C))for j in Q]for i in Q]for k in Q][3]
## looks for green only in the positive direction, rotating 4 times.
## i had trouble finding a good out-of-bounds check that works with the rotation,
## wouldn't be surprised if theres a better idea than min(idx,9)
def p(g,Q=range(10)):C=sum(b'%r'%g)//38%4;return[g:=[[g[j][~i]|8*all(1&g[min(j+3*C-y,9)][~min(i+y,9)]for y in(C,2*C))for j in Q]for i in Q]for k in Q][3]
## inlining the assignment of C doesn't seem to save, since the
## bytesum changes between rotations, and requires a longer
## formula to calculate C (ie. side len of green squares)
p=lambda g,Q=range(10):[g:=[[g[j][~i]|8*all(1&g[min(j+(3-y)*(C:=str(g).count("3")//8+1),9)][~min(i+y*C,9)]for y in(1,2))for j in Q]for i in Q]for k in Q][3]

## older versions:

# slight modification of ovs's solution to remove the need for def.
#  takes 5 seconds because of assignment of `C` being moved into the loop
p=lambda g,Q=range(10):[[g[i][j]|any(all(((g+g[:1]*3)[i+y*[(C:=sum(b'%r'%g)//38%4),-C][S%2]]+g[0])[j+C*[3-y,y-3][S>5]]for y in(1,2))for S in Q)*8for j in Q]for i in Q]

## ovs's version
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]

### ovs (166 bytes)
p=lambda g,Q=range(10):[[g[i][j]|any(all(((g+g[:1]*3)[i+y*(C:=sum(b'%r'%g)//38%4)*(S%-2|1)]+g[0])[j+C*[3-y,y-3][S>5]]for y in(1,2))for S in Q)*8for j in Q]for i in Q]

##

Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]

### combined (169 bytes)
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]
