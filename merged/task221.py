def p(a):r=range(d:=str(a).count('0'));return[[c*(j<9+d*~i)for j in r for c in b]for i in r for b in a]

### ovs (116 bytes)
def p(g):f=sum(g,[]);R=range(s:=9-f.count(max(f)));return[[c*(i*s+j<9-s)for j in R for c in r]for i in R for r in g]
