# mwi (155 vs 139 bytes for gold)
p=lambda g,k=1:-k*g or p([[c//5*c or(u:=2*((a:=r[:x].count(5))==(b:=r[x:].count(5)))+0**a+0**b*3)*(k or c==u)for x,c in enumerate(r)]for r in zip(*g)],k-1)

### combined (159 bytes)
p=lambda i,e=enumerate,s=sum:[[y or(s(x[:b])*2==s(x))*(s(k:=[*map(min,i)])==s(k[:a])*2)*2+0**s(x[b:]+k[a:])*3+0**s(x[:b]+k[:a])for b,y in e(x)]for a,x in e(i)]
