# ovs (70 bytes, gold)
p=lambda a,*n:[b for b in zip(*n or p(a,*a))if{*b}-({*a[1]}&{*a[12]})]

### att (81 bytes)
p=lambda a,*n:[b for b in zip(*n or p(a,*a))if min(c:=sum(a,[]),key=c.count)in b]

### combined (81 bytes)
p=lambda a,*n:[b for b in zip(*n or p(a,*a))if min(c:=sum(a,[]),key=c.count)in b]

### xsot (96 bytes)
import re
p=lambda m:[*map(eval,re.findall((c:=min(s:=str(m)+'[]'*8,key=s.count))+"[^[]*"+c,s))]

###
import re
p=lambda m:[*map(eval,re.findall((c:=min(s:=str(m)+'[]'*8,key=s.count))+"[^[]*"+c,s))]
import re
p=lambda m:[*map(eval,re.findall((c:=min(set(s:=str(m)+'[]'*8),key=s.count))+"[^[]*"+c,s))]
import re
p=lambda m:[*map(eval,re.findall(f"{(c:=min(set(a:=sum(m,[])),key=a.count))}[^[]*{c}",str(m)))]
import re
p=lambda m:[*map(eval,re.findall("%d[^[]*%d"%(c:=min(set(a:=sum(m,[])),key=a.count),c),str(m)))]

def p(m):
 b=min(set(a:=sum(m,[])),key=a.count);N=len(m)
 for i in range(N*N):
  Y=y=i%N;X=x=i//N
  if m[y][x]==b:
   while-~X<N!=m[y][X+1]==b:X+=1
   while-~Y<N!=m[Y+1][x]==b:Y+=1
   return[l[x:X+1]for l in m[y:Y+1]]
