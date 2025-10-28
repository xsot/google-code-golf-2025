# joking (111 bytes, gold)
p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[[l:=l|(b!=y>a<1)*(a:=b),b:=y][y>0]for y in x][::-1],*"*4+"i))))")]

##
p=lambda i,k=3:-k*i or[*map(lambda*x,l=0,b=1,a=1:[0*(l:=l|(b!=y>a<1)*(a:=b))+(b:=y)or l for y in x],*p(i,k-1))][::-1]
import re;p=lambda a,n=-63:n*a or[*zip(*eval(re.sub(r'0(?=[\d, ]*([^0]), (?!0|\1)(\d), 0)',r'\2',str(p(a,n+1)))))][::-1]
p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[0*(l:=l|(b!=y>a<1)*(a:=b))+(b:=y)or l for y in x][::-1],*"*4+"i))))")]
p=lambda i:[i:=[*map(lambda*x,l=0,b=1,a=1:[[l:=l|(b!=y>a<1)*(a:=b),b:=y][y>0]for y in x][::-1],*i)]for _ in i][3]
p=lambda i:exec("i[:]=map(lambda*x,l=0,b=1,a=1:[[l:=l|(b!=y>a<1)*(a:=b),b:=y][y>0]for y in x],*i[::-1]);"*4)or i

### att (123 bytes)
import re
p=lambda a,n=-63:n*a or[*zip(*eval(re.sub(r'0, ([^0])((, (?!0|\1).)+[0, ]*)0',r'0,\1\2\1',str(p(a,n+1)))))][::-1]

### combined (126 bytes)
p=lambda i,k=3:-k*i or[(l:=0)or[y+0*(l:=l|(1>a<y!=b)*b)or l for a,b,y in zip([0,1,*x],[0,*x],x)]for x in zip(*p(i,k-1))][::-1]
