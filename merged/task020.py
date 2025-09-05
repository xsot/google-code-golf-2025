# ovs (173 vs 152 bytes for gold)
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]

### combined (tied, 173 bytes)
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]
