# att (123 vs 115 bytes for gold)
import re
p=lambda a,n=-63:n*a or[*zip(*eval(re.sub(r'0, ([^0])((, (?!0|\1).)+[0, ]*)0',r'0,\1\2\1',str(p(a,n+1)))))][::-1]

### combined (126 bytes)
p=lambda i,k=3:-k*i or[(l:=0)or[y+0*(l:=l|(1>a<y!=b)*b)or l for a,b,y in zip([0,1,*x],[0,*x],x)]for x in zip(*p(i,k-1))][::-1]
