p=lambda a:[[max(sum(a:=[[0,0]]+a,[])[2::3])for _ in r]for r in a]

##

p=lambda g,k=2:[[max(sum(g,[])[(k:=k+1)%3::3])for v in r]for r in g]
