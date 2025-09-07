# ovs (66 vs 62 bytes for gold)
p=lambda a:[[max(sum(a:=[[0,0]]+a,[])[2::3])for _ in r]for r in a]

##

p=lambda g,k=2:[[max(sum(g,[])[(k:=k+1)%3::3])for v in r]for r in g]

### att (67 bytes)
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]

### combined (67 bytes)
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]

### xsot (74 bytes)
p=lambda m,R=range(7):[[max(sum(m,[])[(c+r*7)%3::3])for c in R]for r in R]
