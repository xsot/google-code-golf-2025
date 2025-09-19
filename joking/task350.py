p=lambda i,*n:[[y or(1in{*x[b:]}&{*x[:b]})*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]

##regex solution
import re;p=lambda i,*n:eval(re.sub("1,([^)]+?)(?=1)","1,*[8]*len([\\1]),",str([*zip(*n or p(i,*i))])))

p=lambda i,*n:[(s:=0)or[(y+1in(s:=s|x.pop(0)&1)*x)*8or y for y in[*x]]for*x,in zip(*n or p(i,*i))]

p=lambda i,*n:[*map(lambda*x,b=0:[(y+1in{*x[b:]}&{*x[:(b:=b+1)]})*8or y for y in x],*n or p(i,*i))]