# joking (103 vs 102 bytes for gold)
def p(g):
 y,x,*_=[z.index(max(z))for z in[g]+g]
 for N in b"":g[y+N//3-6][x+N%3-1]=4
 return g

##
def p(g):
 x=y=0
 for _ in g:x+=1>g[0][x];y+=0in g[y]
 for N in b"":g[y+N//3-6][x+N%3-1]=4
 return g

## recursive, not working
p=lambda i,*w:i*0!=0and[*map(p,*sum([[x,x[1:]+x,x[:1]+x]for x in[i,*w]],[]))]or (len({i,*w})==3)*4 or i

### combined (108 bytes)
def p(g):
 x=y=0
 for _ in g:x+=1>g[0][x];y+=0in g[y]
 for N in b"":g[y+N//3-6][x+N%3-1]=4
 return g
