p=lambda i,y=0:[[v|-~int(a:=y*2/sum(c))*(a==(s:=s+v)*2/sum(r)>=v==a%1)for*c,v in zip(*i,r)]for r in i if[y:=y+r[s:=0]]]

##
p=lambda g,k=1:-k*g or p([(a:=0)or[5*(-a+(a:=a+r.pop(0)//5))or(u:=2*(a==(b:=r.count(5)))+0**a+0**b*3)*(k or c==u)for c in[*r]]for*r,in zip(*g)],k-1)