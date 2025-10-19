p=lambda i:[i:=[[sum({v,r[0]}&{*i[1],*r[~(j:=j%5%-3):]})for v in r][::-1]for*r,in zip(*i)if[j:=2]]for _ in i][3]

##
p=lambda i,k=3:-k*i or[*map(lambda s,t,*x:[y*(sum(i,i).count(y)>3>0<y!=s)for y in x[::-1]]+[sum({*x}&{s,t}),s],*p(i,k-1))]

p=lambda i:[i:=[[sum({v,r[0]}&{*i[1],*r[(j:=j%8%-3+1):]})for v in r][::-1]for*r,in zip(*i)if[j:=2]]for _ in i][3]
p=lambda i:[i:=[[sum({v,r[0]}&{*i[1],*r[(j:=j%~7%3)-1:]})for v in r][::-1]for*r,in zip(*i)if[j:=3]]for _ in i][3]
p=lambda i:[i:=[(j:=1)*[sum({v,r[0]}&{*i[1],*r[~(j:=-(j%3&j)):]})for v in r][::-1]for*r,in zip(*i)]for _ in i][3]