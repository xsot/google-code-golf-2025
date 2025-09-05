# combined (69 vs 2500 bytes for gold)
p=lambda i:[[sum({*sum(i,x)},-y)for y in x if y]for x in i if any(x)]

### ovs (84 bytes)
p=lambda g:[[sum({*sum(g,[])})-v for*c,v in zip(*g,r)if any(c)]for r in g if any(r)]


## alternative idea: get row with all colors, reconstruct square from that:

def p(g):*x,=filter(abs,max(g,key=set));return[[x[len(x)//2*(x[0]in{v,y})]for v in x]for y in x]
def p(g):*x,=filter(abs,max(g,key=set));return[[sum({*x}-({v}&{y}or{x[0]}))for v in x]for y in x]
def p(g):*x,=max(g,key=set);*I,=map(x.index,x);return[[x[sum({*I})-min(v,y)]for v in I if v]for y in I if y]
def p(g):*x,=max(g,key=set);T=[sum({*x})-v for v in x if v];return[[[v]*len(T),T][v!=T[0]]for v in T]
def p(g):
 _,a,b={}.fromkeys(sum(g,[]));n=sum(map(bool,max(g)))
 for b in b,[b]*n:a=(p:=~-n//2*[b])+(2-n%2)*[a]+p
 return a
