# ovs (68 bytes, gold)
p=lambda i,r=[]:r*-1*-1or[p(x,sum({*r}or i,x*-1))for x in i if[x]>i]

### combined (69 bytes)
p=lambda i:[[sum({*sum(i,x)},-y)for y in x if y]for x in i if any(x)]
