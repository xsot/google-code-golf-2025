# combined (105 vs 2500 bytes for gold)
p=lambda i,r=range(10):[[max({*i[a][b:]}&{*i[a][:b+1]}|{*c[a:]}&{*c[:a]})for*c,b in zip(*i,r)]for a in r]

### xsot (162 bytes)
def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][8 in m[r][:c]!=8 in m[r][c:]or 8 in a[c::N][:r]!=8 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]

# almost identical to 350
