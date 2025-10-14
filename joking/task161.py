p=lambda m:[[4//(C:=sum(m,m).count)(x)*x|4//C(i)*i for i in m[0]]for x,*_ in m]

##
p=lambda m:[[sum({x,i}-{*sum([*zip(*m[1:9])][1:-1],())})for i in m[0]]for*_,x in m]
p=lambda m:[[sum({x,i}-{*sum([*zip(*m[1:-1])][1:-1],())})for i in m[0]]for*_,x in m]
p=lambda m:[[sum({x,i}-{y for _,*x,_ in m[1:9]for y in x})for i in m[0]]for*_,x in m]