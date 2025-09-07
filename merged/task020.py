# joking (148 vs 149 bytes for gold)
exec(f"def p(g):i,j={'[*map(any,g:=[*zip(*g)])].index(1)+2,'*2};return[g:=[[g[J][I]|((g*2)[i+j-I]*2)[i-j+J]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")

##
def p(g):r=range(10);i,j=[[*map(any,G)].index(1)+2for G in(zip(*g),g)];return[g:=[[g[J][I]|((g*2)[i+j-I]*2)[i-j+J]for I in r]for J in r]for _ in r][3]
exec(f"def p(g):i,j={'[*map(any,g:=[*zip(*g)])].index(1),'*2};return[g:=[[g[J][I]|((g*2)[i+j+4-I]*2)[i-j+J]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")

### ovs (173 bytes)
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]

### combined (173 bytes)
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]
