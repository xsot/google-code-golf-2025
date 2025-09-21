# ovs (174 vs 158 bytes for gold)
def p(g):D,C=sorted({*sum(g,[])}-{0},key=lambda c:str(g).count(f'{c}, '*2));g=[[D*(v==C)for v in r]for r in g];exec("*h,=filter(any,zip(*g));g[:]=h[::len(h)//3];"*2);return g

##

p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in"%s"%x!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)

### combined (208 (209 unzipped) bytes)
p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in str(x)!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)
