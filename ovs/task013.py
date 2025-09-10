def p(i):f,*r=map(i.index,filter(any,i));a=62+f;return[len(x)*[max(i[f+61%(a:=a-1)%(r[0]-f<<1)])]for x in i if i[len(x):]]or[*zip(*p([*zip(*i)]))]

##

def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]
