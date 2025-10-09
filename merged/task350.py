# joking (89 bytes, gold)
p=lambda i:[*map(f:=lambda*x,s=0:[y|(x.count(1)>(s:=s+y%8)>y<1)*8for y in x],*map(f,*i))]

##
p=lambda i:[*map(f:=lambda*x,s=0:[y|(x.count(y+1)>(s:=s+y%8)>0)*8for y in x],*map(f,*i))]
p=lambda i:[*map(f:=lambda*x,b=0:[y|(y+1in{*x[:b]}&{*x[(b:=b+1):]})*8for y in x],*map(f,*i))]

## recursion alt
p=lambda i,*x,b=0:[y|(y+1in{*x[:b]}&{*x[(b:=b+1):]})*8for y in x]or[*map(p,i,*map(p,i*2,*i))]

##regex solution
import re;p=lambda i,*n:eval(re.sub("1,([^)]+?)(?=1)","1,*[8]*len([\\1]),",str([*zip(*n or p(i,*i))])))

p=lambda i,*n:[[y or(1in{*x[b:]}&{*x[:b]})*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
p=lambda i,*n:[(s:=0)or[(y+1in(s:=s|x.pop(0)&1)*x)*8or y for y in[*x]]for*x,in zip(*n or p(i,*i))]

p=lambda i,*n:[*map(lambda*x,b=0:[y|(y+1in{*x[b:]}&{*x[:(b:=b+1)]})*8for y in x],*n or p(i,*i))]

## doesn't work, several cases have > 8 1s
p=lambda i:[*map(f:=lambda*x,s=0:[y|(sum(x)%8>(s:=s+y%8)>y<1)*8for y in x],*map(f,*i))]

### combined (96 bytes)
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
