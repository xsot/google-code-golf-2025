p=lambda i:[*map(f:=lambda*x,s=0:[y|(x.count(1)>(s:=s+y%8)>y<1)*8for y in x],*map(f,*i))]

##
p=lambda i:[*map(f:=lambda*x,s=0:[y|(x.count(y+1)>(s:=s+y%8)>0)*8for y in x],*map(f,*i))]
p=lambda i:[*map(f:=lambda*x,b=0:[y|(y+1in{*x[:b]}&{*x[(b:=b+1):]})*8for y in x],*map(f,*i))]

## recursion alt
p=lambda i,*x,b=0:[y|(y+1in{*x[:b]}&{*x[(b:=b+1):]})*8for y in x]or[*map(p,i,*map(p,i*2,*i))]

##regex solution
import re;p=lambda i,*n:eval(re.sub("1,([^)]+?)(?=1)","1,*[8]*len([\\1]),",str([*zip(*n or p(i,*i))])))

p=lambda i,*n:[[y or(1in{*x[b:]}&{*x[:b]})*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
p=lambda i,*n:[(s:=0)or[(y+1in(s:=s|x.pop(0)&1)*x)*8or y for y in[*x]]for*x,in zip(*n or p(i,*i))]

p=lambda i,*n:[*map(lambda*x,b=0:[y|(y+1in{*x[b:]}&{*x[:(b:=b+1)]})*8for y in x],*n or p(i,*i))]

## doesn't work, several cases have > 8 1s
p=lambda i:[*map(f:=lambda*x,s=0:[y|(sum(x)%8>(s:=s+y%8)>y<1)*8for y in x],*map(f,*i))]