# att (139 bytes, gold)
p=lambda a,n=87,i=0:[[min(b+c,key=b.count)for c in zip(*a)]for b in-n*a]or p([*zip(*a[(6in(i:=1+i*(a==(a:=b))for b in a[-1]))-2::-1])],n-1)

### joking (164 bytes)
p=lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in range(5**6)if len({*str(s:=[r[y//625:][:10-y//5%5]for r in(i*9)[y//25%25:][:10-y%5]])})<7][0]

## faster for +1b
p=lambda i:next([[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in range(5**6)if len({*str(s:=[r[y//625:][:10-y//5%5]for r in(i*9)[y//25%25:][:10-y%5]])})<7)

## alas, recursion limit
p=lambda i,y=0:len({*str(s:=[r[y//625:][:10-y//5%5]for r in(i*9)[y//25%25:][:10-y%5]])})<7and[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]or p(i,y+1)

##
p=lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in range(5**6)if len({*str(s:=[r[y//625:][:10-y//5%5]for r in i[y//25%25:][:10-y%5]])})<7and s[5:]][0]
p=lambda i,r=range(25):[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in r for x in r for a in r if len({*str(s:=[r[y:y+10-a//5]for r in i[x:x+10-a%5]])})<7and s[5:]][0]
p=eval("lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]"+"for %s in range(25)"*3%(*'yxa',)+"if len({*str(s:=[r[y:y+10-a//5]for r in i[x:x+10-a%5]])})<7and s[5:]][0]")

### ovs (226 (235 unzipped) bytes)
p=lambda g:max([[min(w:=r+c,key=w.count)for*c,in zip(*S)]for r in S]for A in range(len(g.pop(0))-6)if(s:=lambda w:len({*sum([r[A:A+6]for r in g[:6]],w[:6])})<=2)for S in[[[v for v,*c in zip(r,*g)if s(c)]for r in g if s(r[A:])]])or p(g)

### combined (231 bytes)
p=lambda i,x=0:(k:=[z for a in range(225)if len(z:=[t[x%30:][:a%15]for t in i[x//30:][:a//15]])>5<len(z[0])>2==len({*sum(z,[])})])and[[max(s-{*k[-1][0]})if len(s:={*y,*x})>1else y[0]for y in zip(x,*k[-1])]for x in k[-1]]or p(i,x+1)
