# combined (213 (223 unzipped) vs 204 bytes for gold)
def p(i,r=range(10)):I=[r*2for r in i*2];return[[[max(I[x][y],I[a+n+b+~y][b-a+x],I[a-b+y][b+n+a+~x],I[2*a+n+~x][2*b+n+~y])for y in r]for x in r]for n in(4,3,2)for a in r for b in r if all(all(x[b:b+n])for x in I[a:a+n])][0]
