# att (152 vs 2500 bytes for gold)
p=lambda a,n=-3:n*a or[[d:=[e:=b.pop(),d][g[2]!=d>0<e!=g[1]in b]for _ in[*b]]for*b,in zip(*p(a,n+1))if[d:=0,g:=sorted(set(c:=sum(a,a[5])),key=c.count)]]

### joking (165 bytes)
import re
def p(i,k=3):r=sum(i,i[5]);a,b,c=sorted({*r},key=r.count);return-k*i or eval(re.sub(f"{b},({[a,c]}+{a})",r"b,*[a]*len([\1])",str([*zip(*p(i,k-1)[::-1])])))

### combined (184 bytes)
p=lambda i,k=7:-k*i or[[(y==(t:=sorted({*(r:=sum(i,[]))},key=r.count))[2]!=t[0]in x[b:]!=t[1]in x[:b])*t[x[b:].count(t[0])>2]or y for b,y in enumerate(x)]for x in zip(*p(i,k-1))][::-1]
