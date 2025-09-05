# xsot (105 vs 2500 bytes for gold)
p=lambda m:[[sum(({x}&{y}|{i}&{j})&{min(a:=sum(m,[]),key=a.count)})for i,*_,j in zip(*m)]for x,*_,y in m]

### combined (109 bytes)
p=lambda i:[[sum(({x[0]}&{x[-1]}|{s[0]}&{s[-1]})&{min(k:=sum(i,[]),key=k.count)})for s in zip(*i)]for x in i]
