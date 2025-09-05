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