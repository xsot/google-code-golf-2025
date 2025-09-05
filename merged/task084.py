# joking (63 vs 62 bytes for gold)
def p(i,x=1):
 while i[x:]:i[-1][x]=4;i[~x][x]=2;x+=1
 return i


## alt 63s
def p(i,x=0):
 for r in i[:-1]:x-=1;i[-1][x]=4;r[x]=2
 return i

def p(i,x=-1):
 for r in i[:x]:i[-1][x]=4;r[x]=2;x-=1
 return i

### combined (64 bytes)
def p(i,x=1):i[-1][x]=4;i[~x][x]=2;return i[:~x]and p(i,x+1)or i

### ovs (65 bytes)
def p(g,i=0):
 while g[1-i:]:i-=1;g[~i][i]=2;g[-1][i]=4
 return g
