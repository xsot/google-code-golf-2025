# ovs (100 bytes, gold)
p=lambda i,*I:[[W[b]|sum({*w[b:]}&{*w[:b]})for b in range(10)]for*W,w in zip(*I or p(zip(*i),*i),i)]

### combined (105 bytes)
p=lambda i,r=range(10):[[max({*i[a][b:]}&{*i[a][:b+1]}|{*c[a:]}&{*c[:a]})for*c,b in zip(*i,r)]for a in r]

### xsot (162 bytes)
def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][8 in m[r][:c]!=8 in m[r][c:]or 8 in a[c::N][:r]!=8 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]

# almost identical to 350
