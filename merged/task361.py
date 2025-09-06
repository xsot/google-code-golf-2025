# xsot (195 (245 unzipped) vs 203 bytes for gold)
def p(a):I=[a*2for a in a+a];return[[[max(I[x][y],I[a+b+n+~y][b-a+x],I[a-b+y][a+b+n+~x],I[a+a+n+~x][b+b+n+~y])for y in range(10)]for x in range(10)]for n in range(10)for a in range(10)for b in range(10)if all(all(x[b:b+n])for x in I[a:a+n])][-1]

### mwi (208 (241 unzipped) bytes)
def p(i):I=[r*2for r in i*2];return[[[max(I[x][y],I[a+n+b+~y][b-a+x],I[a-b+y][b+n+a+~x],I[2*a+n+~x][2*b+n+~y])for y in range(10)]for x in range(10)]for n in(4,3,2)for a in range(10)for b in range(10)if all(all(x[b:b+n])for x in I[a:a+n])][0]

### ovs (210 (223 unzipped) bytes)
def p(i,r=range(10)):I=[r*2for r in i*2];return[[[max(I[x][y],I[a+n+b+~y][b-a+x],I[a-b+y][b+n+a+~x],I[2*a+n+~x][2*b+n+~y])for y in r]for x in r]for n in(4,3,2)for a in r for b in r if all(all(x[b:b+n])for x in I[a:a+n])][0]

### combined (210 (223 unzipped) bytes)
def p(i,r=range(10)):I=[r*2for r in i*2];return[[[max(I[x][y],I[a+n+b+~y][b-a+x],I[a-b+y][b+n+a+~x],I[2*a+n+~x][2*b+n+~y])for y in r]for x in r]for n in(4,3,2)for a in r for b in r if all(all(x[b:b+n])for x in I[a:a+n])][0]
