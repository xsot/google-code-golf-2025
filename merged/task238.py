# compression_experiments (201 (313 unzipped) bytes, gold)
def p(i):r=[e for e in zip(*[e for e in zip(*i)if{*e}-{0}-{8}])if{*e}-{0}-{8}];return[[[*[f:=[e for e in zip(*[e for e in zip(*i)if{*e}-{0}&{8}])if{*e}-{0}&{8}],*f,f][n],*r[n]][e-1]and(r[1-(len(r)-e-1>n<e)|-(len(r)-e-1<n>e)][1-(len(r)-e-1>n>e)|-(len(r)-e-1<n<e)]or 8)for e in range(len(r))]for n in range(len(r))]

### joking (202 (313 unzipped) bytes)
def p(a):b=[j for j in zip(*[j for j in zip(*a)if{*j}-{0}-{8}])if{*j}-{0}-{8}];return[[[*[c:=[j for j in zip(*[j for j in zip(*a)if{*j}-{0}&{8}])if{*j}-{0}&{8}],*c,c][i],*b[i]][j-1]and(b[1-(len(b)-j-1>i<j)|-(len(b)-j-1<i>j)][1-(len(b)-j-1>i>j)|-(len(b)-j-1<i<j)]or 8)for j in range(len(b))]for i in range(len(b))]

### att (207 (305 unzipped) bytes)
def p(a):b=[j for j in zip(*[j for j in zip(*a)if{*j}-{0,8}])if{*j}-{0,8}];return[[[*[c:=[j for j in zip(*[j for j in zip(*a)if{*j}-{0}&{8}])if{*j}-{0}&{8}],*c,c][i],*b[i]][j-1]and(b[1-(j>i<len(b)+~j)|-(j<i>len(b)+~j)][1-(j<i<len(b)+~j)|-(j>i>len(b)+~j)]or 8)for j in range(len(b))]for i in range(len(b))]

## 213
def p(a):b,c=eval(f"{'[b for*b,in zip(*'*2}a{')if{*b}-{0}%s{8}]'*2},"*2%(*'--&&',));r=range(l:=len(b));return[[(b[i]+[c,*c,c][i])[-(F:=l+~j)]and(b[1-(F>i<j)|-(j<i>F)][1-(j<i<F)|-(j>i>F)]or 8)for j in r]for i in r]

### ovs (216 (313 unzipped) bytes)
def p(i):m=[[a[0]for a in zip(b,*i)if{*a}-{0,8}]for b in i if{*b}-{0,8}];return[[a<len(m)-1>b>0and((k:=[[a[0]for a in zip(b,*i)if{*a}&{8}]for b in i if{*b}&{8}][a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

## 237 bytes without compression:

def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*b'	'}]];r=range(f:=len(m));return[[[*[*l,[b%~-f]*f][a-1],a%~-f][b-1]and(m[1-((F:=f+~b)>a<b)|-(b<a>F)][1-(b<a<F)|-(b>a>F)]or 8)for b in r]for a in r]

### mwi (222 (282 unzipped) bytes)
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and((k:=l[a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]

### combined (231 (247 unzipped) bytes)
def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*range(1,8),9}]];f=len(m)-1;r=range(f+1);return[[a<f>b>0and((k:=l[a-1][b-1])and m[1-(b>a<f-b)|-(b<a>f-b)][1-(b<a<f-b)|-(b>a>f-b)]or k)or m[a][b]for b in r]for a in r]
