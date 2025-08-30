# joking+mwi (234 (247 unzipped) vs 228 bytes for gold)
def p(i):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{8},{*range(1,8),9}]];f=len(m)-1;r=range(f+1);return[[a<f>b>0and((k:=l[a-1][b-1])and m[1-(b>a<f-b)|-(b<a>f-b)][1-(b<a<f-b)|-(b>a>f-b)]or k)or m[a][b]for b in r]for a in r]
