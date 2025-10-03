# ovs (109 bytes, gold)
p=lambda i:[i:=[*zip(*(i[:1]*11+[x for x in i if{sum(x),0}^{*x+max(i,key=any)}])[:~len(i):-1])]for _ in i][3]

### joking (116 bytes)
p=lambda i,k=3,*h:-k*i or p([*zip(*([x for x in i if len(h:={*h,*x})-3+sum(x)-max(x)]+i[:1]*13)[len(i)-1::-1])],k-1)

### combined (120 bytes)
p=lambda i,k=3,h={0}:-k*i or p([*zip(*([x for x in i if len(h:=h|{*x})-3+sum(x)-max(x)]+i[-1:]*99)[:len(i)])][::-1],k-1)
