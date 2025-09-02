import re
def p(i,k=3):r=sum(i,i[5]);a,b,c=sorted({*r},key=r.count);return-k*i or eval(re.sub(f"{b},({[a,c]}+{a})",r"b,*[a]*len([\1])",str([*zip(*p(i,k-1)[::-1])])))