# att (73 vs 72 bytes for gold)
p=lambda a,b=45:[*zip(*[2*((b:=b-1)*[0]+a[0])for c in 5*a[0]if c])][b:45]

##
def p(a):b,=a;i=45;return[*zip(*[2*((i:=i-1)*[0]+b)for c in b*5if c])][i:45]
def p(a):b,=a;l=25-5*b.count(0);return[((~-l*[0]+b)*2)[i:i+l]for i in range(l)]
def p(a):b,=a;c=5*len({*b}-{0})*[i:=0];return[c[(i:=i+1):]+(b+c)[:i]for _ in c]
def p(a):b,=a;c=[i:=0for c in b*5if c];return[c[(i:=i+1):]+(b+c)[:i]for _ in c]

### combined (80 bytes)
def p(a):l=25-5*a[0].count(0);return[((~-l*[0]+a[0])*2)[i:i+l]for i in range(l)]

### xsot (84 bytes)
def p(a):
 m,*a=a;m+=(4-m.count(0))*5*[0]
 for _ in m:a=[m]+a;m=[0]+m[:-1]
 return a

##
def p(a):
 m=a.pop();m+=(4-m.count(0))*5*[0]
 for _ in m:a=[m]+a;m=[0]+m[:-1]
 return a
