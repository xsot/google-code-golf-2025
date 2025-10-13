# joking (55 bytes, gold)
# i blacked out and this was here when i woke up
p=lambda i,s=[],k=3:-k*i or p([*zip(*i+s)],i[::-1],k-1)

### ovs (72 bytes)
S='[::-1]for*x,a in zip(*i,i)]';p=eval(f'lambda i:[a+x{S}+[x+a'+S+S[:6])

##

p=lambda g,i=0:g[i:]and[w:=g[i]+[*[*zip(*g)][i]][::-1],*p(g,i+1),w[::-1]]

### combined (75 bytes)
p=lambda i:(s:=[a+x for a,*x in zip(i,*i[::-1])])+[x[::-1]for x in s[::-1]]
