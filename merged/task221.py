# joking+mwi (102 vs 94 bytes for gold)
def p(i):j=3*str(i).count("0");return[[(a//3*j+b<27-j)*i[a%3][b%3]for b in range(j)]for a in range(j)]

### att (103 bytes)
def p(a):r=range(d:=str(a).count('0'));return[[c*(j<9+d*~i)for j in r for c in b]for i in r for b in a]

### ovs (116 bytes)
def p(g):f=sum(g,[]);R=range(s:=9-f.count(max(f)));return[[c*(i*s+j<9-s)for j in R for c in r]for i in R for r in g]
