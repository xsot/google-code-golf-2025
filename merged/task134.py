# ovs (123 bytes, gold)
p=lambda g,D=10:[[D*(D!=v>0)for v in r]for r in('0, %g, 0'%D in'%s'%g)*g]or(h:=[*filter(any,zip(*p(g,D-.5)))])[::len(h)//3]

##

p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in"%s"%x!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)

### joking (128 bytes)
p=lambda g,D=10:(G:=[[D*(D!=v>0)for v in r]for r in('0, %g, 0'%D in'%s'%g)*g])or(h:=[*filter(any,zip(*p(g,D-.5)))])[::len(h)//3]

### combined (208 (209 unzipped) bytes)
p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in str(x)!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)
