# att (79 vs 77 bytes for gold)
def p(a):b,=a;l=25-5*b.count(0);return[((~-l*[0]+b)*2)[i:i+l]for i in range(l)]

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
