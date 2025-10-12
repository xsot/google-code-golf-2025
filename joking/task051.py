p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[[l:=l|(b!=y>a<1)*(a:=b),b:=y][y>0]for y in x][::-1],*"*4+"i))))")]

##
p=lambda i,k=3:-k*i or[*map(lambda*x,l=0,b=1,a=1:[0*(l:=l|(b!=y>a<1)*(a:=b))+(b:=y)or l for y in x],*p(i,k-1))][::-1]
import re;p=lambda a,n=-63:n*a or[*zip(*eval(re.sub(r'0(?=[\d, ]*([^0]), (?!0|\1)(\d), 0)',r'\2',str(p(a,n+1)))))][::-1]
p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[0*(l:=l|(b!=y>a<1)*(a:=b))+(b:=y)or l for y in x][::-1],*"*4+"i))))")]