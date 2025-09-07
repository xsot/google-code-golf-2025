# joking (150 vs 140 bytes for gold)
def p(i):f,*r=map(i.index,filter(any,i));a=~f;return[[max(i[f+(0>(a:=a+1)or a)%(2*r[0]-2*f)])]*len(x)for x in i if i[len(x):]]or[*zip(*p([*zip(*i)]))]

### ovs (169 bytes)
def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]

### combined (169 bytes)
def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]
