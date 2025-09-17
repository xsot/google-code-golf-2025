# ovs (216 (313 unzipped) bytes, gold)
def p(i):m=[[a[0]for a in zip(b,*i)if{*a}-{0,8}]for b in i if{*b}-{0,8}];return[[a<len(m)-1>b>0and((k:=[[a[0]for a in zip(b,*i)if{*a}&{8}]for b in i if{*b}&{8}][a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

## 237 bytes without compression:

def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*b'	'}]];r=range(f:=len(m));return[[[*[*l,[b%~-f]*f][a-1],a%~-f][b-1]and(m[1-((F:=f+~b)>a<b)|-(b<a>F)][1-(b<a<F)|-(b>a>F)]or 8)for b in r]for a in r]

### mwi (222 (282 unzipped) bytes)
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and((k:=l[a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

### combined (231 (247 unzipped) bytes)
def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*range(1,8),9}]];f=len(m)-1;r=range(f+1);return[[a<f>b>0and((k:=l[a-1][b-1])and m[1-(b>a<f-b)|-(b<a>f-b)][1-(b<a<f-b)|-(b>a>f-b)]or k)or m[a][b]for b in r]for a in r]
