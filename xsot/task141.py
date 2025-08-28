p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]

##
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(abs(r-(i:=(a:=sum(m,[])).index(e:=max(a)))//N)==abs(c-i%N))*e for c in R]for r in R]
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(*{*a}-{0})]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]