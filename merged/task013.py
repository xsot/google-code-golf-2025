# ovs (136 vs 124 bytes for gold)
def p(i):*v,=map(max,*i);*_,f,r=sorted(map(v.index,v));N=len(v);return i[N:]and[*zip(*p([*zip(*i)]))]or[(v[:f]+v[f:2*r-f]*N)[:N]]*len(i)

##

def p(i):f,*r=map(i.index,filter(any,i));a=62+f;return[len(x)*[max(i[f+61%(a:=a-1)%(r[0]-f<<1)])]for x in i if i[len(x):]]or[*zip(*p([*zip(*i)]))]

def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]

### joking (150 bytes)
def p(i):f,*r=map(i.index,filter(any,i));a=~f;return[[max(i[f+(0>(a:=a+1)or a)%(2*r[0]-2*f)])]*len(x)for x in i if i[len(x):]]or[*zip(*p([*zip(*i)]))]

### combined (169 bytes)
def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]
