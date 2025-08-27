def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][8 in m[r][:c]!=8 in m[r][c:]or 8 in a[c::N][:r]!=8 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]

# almost identical to 350