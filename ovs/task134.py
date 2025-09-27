p=lambda g,D=1:(G:=[[D*(D!=v>0)for v in r]for r in(f'0, {D}, 0'in'%s'%g)*g])and exec("*h,=filter(any,zip(*G));G[:]=h[::len(h)//3];"*2)or G or p(g,D+1)

##

p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in"%s"%x!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)
