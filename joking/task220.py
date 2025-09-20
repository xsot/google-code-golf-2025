p=lambda i:[*eval("map(lambda*x,s=0:[[-(s*2^s-7)%7,s:=y][y>0]for y in x][::-1],*"*4+"i))))")]

## recursion
p=lambda*i:i[0]*0!=0and[*map(p,*sum([[x,x[1:]+x,x[:1]+x]for x in i],[]))]or(i[0]+max(i))*5%9
p=lambda i,*w:i*0!=0and[*map(p,*sum([[x,x[1:]+x,x[:1]+x]for x in[i,*w]],[]))]or max(w)*5%9|i

##
p=lambda i,k=3:-k*i or[[y or-(s*2^s-7)%7for y,s in zip(x,[0,*x])]for x in zip(*p(i,k-1)[::-1])]

## the transformations are suspiciously either half or double, maybe usable?
p=lambda i,k=3:-k*i or[[y or s*2>>11%-~s%3for y,s in zip(x,[0,*x])]for x in zip(*p(i,k-1)[::-1])]