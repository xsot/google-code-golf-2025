# ovs (87 bytes, gold)
def p(i):j=str(i).count("0");a=2;return[(q*(9-(a:=a+1)//3*j)+[0]*21)[:j*3]for q in i*j]

##

def p(g):f=sum(g,[]);R=range(s:=9-f.count(max(f)));return[[c*(i*s+j<9-s)for j in R for c in r]for i in R for r in g]

### joking (98 bytes)
def p(i):r=range(j:=3*str(i).count("0"));return[[(a//3*j+j+b<27)*i[a%3][b%3]for b in r]for a in r]

### combined (102 bytes)
def p(i):j=3*str(i).count("0");return[[(a//3*j+b<27-j)*i[a%3][b%3]for b in range(j)]for a in range(j)]

### att (103 bytes)
def p(a):r=range(d:=str(a).count('0'));return[[c*(j<9+d*~i)for j in r for c in b]for i in r for b in a]
