p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted([c:=-b.count(e)]+[e]*-c+[0]*11for e in{*b})))][2:]

##

def p(g):f=sum(g,[]);q=f.count;C=sorted({*f},key=q)[::-1];return[[c*(q(c)>i)for c in C]for i in range(q(C[0]))]
