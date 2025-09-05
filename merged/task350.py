# combined (96 vs 2500 bytes for gold)
p=lambda i,*n:[[y or(1in x[b:]!=1in x[:b])*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]

### xsot (162 bytes)
def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][1 in m[r][:c]!=1 in m[r][c:]or 1 in a[c::N][:r]!=1 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]

########
def p(m):M,N=len(m),len(m[0]);a=sum(m,[]);return[[[m[r][c],m[r][c]or 8][1 in m[r][:c]!=1 in m[r][c:]or 1 in a[c::N][:r]!=1 in a[c::N][r:]]for c in range(N)]for r in range(M)]

def p(m):
    M,N=len(m),len(m[0])
    a=sum(m,[])
    for i in range(M*N):
        r=i//N;c=i%N
        if 1 in m[r][:c]!=1 in m[r][c:] or 1 in a[c::N][:r]!=1 in a[c::N][r:]:
            m[r][c]=a[i]or 8
    return m

def p(m):
    M,N=len(m),len(m[0])
    a=sum(m,[])
    for r in range(M):
        for c in range(N):
            if 1 in m[r][:c]and 1 in m[r][c:] or 1 in a[c::N][:r] and 1 in a[c::N][r:]:
                m[r][c] = m[r][c] or 8
    return m
