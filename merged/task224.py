# ovs (154 vs 138 bytes for gold)
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[^)]*[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]

##
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(" 0(?=,"+["[^)]*[^5]*$)"," 0.0|, 5)"][k<4],["0.",max({*str(g)}-{*"[5]"})][k<4],str([*zip(*g)][::-1]))),k-1)
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(*[" 0(?=,[^)]*[^5]*$)","0."," 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})][k<4::2],str([*zip(*g)][::-1]))),k-1)


def p(g):E=enumerate;(y,*_,Y),(x,*_,X)=map(sorted,zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]));f=sum(g,[]);c,={*f}-{0,5};return[[v|c*((x<j<X)*(i in{y+1,Y-1})|(y<i<Y)*(j in{x+1,X-1}))for j,v in E(r)]for i,r in E(g)]

### mwi (157 bytes)
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[0, ]*5?[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]

### joking (165 bytes)
# feels golfable
p=lambda i,k=3,s=0,S=sum:-k*i or p([[y|(s==5in{*(h:=[*map(S,i)])[b+1:]}&{*h[:b]})*S({*S(i,[-5])})for b,y in enumerate(x)]+0*[s:=s*2+S(x)]for x in zip(*i)][::-1],k-1)

## no enumerate
p=lambda i,k=3,s=0:-k*i or p([[s:=s*2+max(x),b:=0]and[y|(5in{*(h:=[*map(max,i)])[:b]}&{*h[(b:=b+1):]}!=5<s<20)*sum({*sum(i,[])},-5)for y in x]for x in zip(*i)][::-1],k-1)

### combined (171 bytes)
p=lambda i,k=3,s=0:-k*i or p([[y or(s==5in{*(h:=[*map(max,i)])[b+1:]}&{*h[:b]})*sum({*sum(i,[])},-5)for b,y in enumerate(x)]*1**(s:=s*2+max(x))for x in zip(*i)][::-1],k-1)
