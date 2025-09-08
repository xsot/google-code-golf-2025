def p(i):j=str(i).count("0");a=2;return[(q*(9-(a:=a+1)//3*j)+[0]*21)[:j*3]for q in i*j]

##

def p(g):f=sum(g,[]);R=range(s:=9-f.count(max(f)));return[[c*(i*s+j<9-s)for j in R for c in r]for i in R for r in g]
