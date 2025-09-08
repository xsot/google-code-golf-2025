# joking (122 vs 119 bytes for gold)
p=lambda i,k=3:-k*i or[*map(lambda s,t,*x:[y*(sum(i,i).count(y)>3>0<y!=s)for y in x[::-1]]+[sum({*x}&{s,t}),s],*p(i,k-1))]

### combined (133 bytes)
p=lambda i,k=3:-k*i or[[x[0],sum({*x[1:]}&{*x[:2]}),*[y*(sum(i,i).count(y)>4>0<y!=x[0])for y in x[2:]]]for x in zip(*p(i,k-1)[::-1])]
