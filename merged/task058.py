# att (94 bytes, gold)
p=lambda a:a and[len(b:=a[0])*[3],[*b[:~(c:=3*[b]>a)]]+[3]*-~c,*zip(*p([*zip(*a[2:])])[::-1])]

### joking (111 bytes)
def p(i,k=7):r=range(l:=len(i));return-k*i or p([[i[~b][a]|~a%2*(a-2/k<b<l-a-30%k)*3for b in r]for a in r],k-2)

##
p=lambda i,k=22,s=0:-k*i or[[(len(x)-k>=0==y+s==a-k//4*2)*3+(s:=y)for y in x]for a,x in enumerate(zip(*p(i,k-1)))][::-1]
def p(i,k=7):r=range(l:=len(i));return-k*i or p([[i[~b][a]or~a%2*(a-1//k<=b<l-a-30%k)*3for b in r]for a in r],k-2)

### combined (127 bytes)
p=lambda i,k=42:[[y+(len(x)-k>=0==y+s<=a==k//4*2)*3for y,s in zip(x,[0,*x])]for a,x in enumerate(zip(*-k*i or p(i,k-1)))][::-1]
