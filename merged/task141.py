# joking (100 vs 94 bytes for gold)
exec("p=lambda i:[[max((k:=i[t]+[0]*29)[b+t-a]|k[b-t+a]"+"for %s in range(len(i))%s"*3%(*'t)b]a]',))

### ovs (102 bytes)
def p(i):e=range(len(i));return[[max((k:=i[t]+[0]*29)[b+t-a]|k[b-t+a]for t in e)for b in e]for a in e]

##

p=eval('lambda i:list(list(max((k:=i[t]+[0]*29)[b+t-a]|k[b-t+a]'+"for %s in range(len(i)))"*3%(*'tba',))

### combined (106 bytes)
p=lambda i,e=enumerate:[[max((k:=z+[0]*99)[t+b-a]|k[a+b-t]for t,z in e(i))for b,y in e(x)]for a,x in e(i)]

### xsot (119 bytes)
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]

##
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(abs(r-(i:=(a:=sum(m,[])).index(e:=max(a)))//N)==abs(c-i%N))*e for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(*{*a}-{0})]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
