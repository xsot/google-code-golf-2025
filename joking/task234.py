p=lambda i:[i:=[*zip(*[x for x in i[:1]*11+i if{sum(x),0}^{*x+max(i,key=any)}][:~len(i):-1])]for _ in i][3]

##
p=lambda i,k=3,*h:-k*i or p([*zip(*([x for x in i if len(h:={*h,*x})-3+sum(x)-max(x)]+i[:1]*13)[len(i)-1::-1])],k-1)