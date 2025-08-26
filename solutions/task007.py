p=lambda g,k=2:[[max(sum(g,[])[(k:=k+1)%3::3])for v in r]for r in g]

### xsot (74 bytes)
p=lambda m,R=range(7):[[max(sum(m,[])[(c+r*7)%3::3])for c in R]for r in R]

##
p=lambda m,R=range(7):[[max(sum(m,[])[(c+r*7)%3::3])for c in R]for r in R]
