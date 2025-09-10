S='+~-~[*map(any,g:=[*zip(*g)])].index(1)'*2
p=eval(f"lambda g:[g:=[[g[J][I]|((g*2)[-(I{S})]*2)[J-{S}]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")

##

r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]
