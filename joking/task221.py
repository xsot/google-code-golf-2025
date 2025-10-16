def p(i):j=sum(i,i).count(a:=0);return[(q*(9+(a:=a-1)//3*j)+[0]*21)[:j*3]for q in i*j]

##
def p(i):r=range(j:=3*str(i).count("0"));return[[(a//3*j+j+b<27)*i[a%3][b%3]for b in r]for a in r]