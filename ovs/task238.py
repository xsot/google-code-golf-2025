def p(i):m=[[a[0]for a in zip(b,*i)if{*a}-{0,8}]for b in i if{*b}-{0,8}];return[[a<len(m)-1>b>0and((k:=[[a[0]for a in zip(b,*i)if{*a}&{8}]for b in i if{*b}&{8}][a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

## 237 bytes without compression:

def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*b'	'}]];r=range(f:=len(m));return[[[*[*l,[b%~-f]*f][a-1],a%~-f][b-1]and(m[1-((F:=f+~b)>a<b)|-(b<a>F)][1-(b<a<F)|-(b>a>F)]or 8)for b in r]for a in r]
