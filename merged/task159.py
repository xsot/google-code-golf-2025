# combined (185 vs 2500 bytes for gold)
def p(i,e=enumerate):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{2},{1,*range(3,10)}]];s=len(l)//3;return[[y or m[~-a//s][~-b//s]for b,y in e(x)]for a,x in e(l)]
