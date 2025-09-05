# joking (104 bytes, gold)
p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted({(e,~e)*b.count(e)+(0,)*99for e in b},key=sum)))][1::2]

### att (108 bytes)
p=lambda a,i=0:[b:=sum(a,[]),c:=b.count]*any(r:=sorted([e*(c(e)>i)for e in{*b}],key=c)[::-1])and[r]+p(a,i+1)

### combined (108 bytes)
def p(i):z=sum(i,[]);c=z.count;return[*filter(sum,zip(*[[y]*c(y)+[0]*11for y in sorted({*z},key=c)][::-1]))]

### ovs (111 bytes)
def p(g):f=sum(g,[]);q=f.count;C=sorted({*f},key=q)[::-1];return[[c*(q(c)>i)for c in C]for i in range(q(C[0]))]
