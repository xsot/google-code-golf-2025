# combined (106 vs 96 bytes for gold)
p=lambda i,e=enumerate:[[max((k:=z+[0]*99)[t+b-a]|k[a+b-t]for t,z in e(i))for b,y in e(x)]for a,x in e(i)]

### xsot (119 bytes)
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]

##
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(abs(r-(i:=(a:=sum(m,[])).index(e:=max(a)))//N)==abs(c-i%N))*e for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(*{*a}-{0})]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
