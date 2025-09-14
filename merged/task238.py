# mwi (222 (282 unzipped) vs 223 bytes for gold)
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and((k:=l[a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

### ovs (tied, 222 (287 unzipped) bytes)
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and(l[a-1][b-1]and m[1-(len(m)-1-b>a<b)|-(len(m)-1-b<a>b)][1-(len(m)-1-b>a>b)|-(len(m)-1-b<a<b)]or l[a-1][b-1])or m[a][b]for b in range(len(m))]for a in range(len(m))]
#

### combined (231 (247 unzipped) bytes)
def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*range(1,8),9}]];f=len(m)-1;r=range(f+1);return[[a<f>b>0and((k:=l[a-1][b-1])and m[1-(b>a<f-b)|-(b<a>f-b)][1-(b<a<f-b)|-(b>a>f-b)]or k)or m[a][b]for b in r]for a in r]
