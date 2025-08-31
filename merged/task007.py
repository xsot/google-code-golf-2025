# att (67 vs 65 bytes for gold)
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]

### combined (tied, 67 bytes)
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]

### ovs (68 bytes)
p=lambda g,k=2:[[max(sum(g,[])[(k:=k+1)%3::3])for v in r]for r in g]

### xsot (74 bytes)
p=lambda m,R=range(7):[[max(sum(m,[])[(c+r*7)%3::3])for c in R]for r in R]
