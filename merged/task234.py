# combined (120 vs 2500 bytes for gold)
p=lambda i,k=3,h={0}:-k*i or p([*zip(*([x for x in i if len(h:=h|{*x})-3+sum(x)-max(x)]+i[-1:]*99)[:len(i)])][::-1],k-1)
