# ovs (125 bytes, gold)
p=lambda i,y=0:[[-s+(s:=s+v)or-~int(a:=y*2/sum(c))*(a==s*2/sum(r)>=0==a%1)for*c,v in zip(*i,r)]for r in i if[s:=0,y:=y+r[0]]]

### joking (148 bytes)
p=lambda g,k=1:-k*g or p([(a:=0)or[5*(-a+(a:=a+r.pop(0)//5))or(u:=2*(a==(b:=r.count(5)))+0**a+0**b*3)*(k or c==u)for c in[*r]]for*r,in zip(*g)],k-1)

### mwi (155 bytes)
p=lambda g,k=1:-k*g or p([[c//5*c or(u:=2*((a:=r[:x].count(5))==(b:=r[x:].count(5)))+0**a+0**b*3)*(k or c==u)for x,c in enumerate(r)]for r in zip(*g)],k-1)

### combined (159 bytes)
p=lambda i,e=enumerate,s=sum:[[y or(s(x[:b])*2==s(x))*(s(k:=[*map(min,i)])==s(k[:a])*2)*2+0**s(x[b:]+k[a:])*3+0**s(x[:b]+k[:a])for b,y in e(x)]for a,x in e(i)]
