# ovs (115 bytes, gold)
p=lambda i:[i:=[[sum({v,r[0]}&{r[-1],*i[1],*r[j**5:]})for j,v in enumerate(r)][::-1]for*r,in zip(*i)]for _ in i][3]
# enumerate + [::-1] looks a bit annoying

### joking (122 bytes)
p=lambda i,k=3:-k*i or[*map(lambda s,t,*x:[y*(sum(i,i).count(y)>3>0<y!=s)for y in x[::-1]]+[sum({*x}&{s,t}),s],*p(i,k-1))]

### combined (133 bytes)
p=lambda i,k=3:-k*i or[[x[0],sum({*x[1:]}&{*x[:2]}),*[y*(sum(i,i).count(y)>4>0<y!=x[0])for y in x[2:]]]for x in zip(*p(i,k-1)[::-1])]
