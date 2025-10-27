# ovs (131 bytes, gold)
p=lambda g,k=6,w=0:~k*g or[[a+[(0is a<w<=k)*max({*sum(g,r)}-{5}),0.][2>w]for a in r]for*r,in zip(*p(g,k-1))if[w:=w*2+any(r)]][::-1]

##
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[^)]*[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(" 0(?=,"+["[^)]*[^5]*$)"," 0.0|, 5)"][k<4],["0.",max({*str(g)}-{*"[5]"})][k<4],str([*zip(*g)][::-1]))),k-1)
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(*[" 0(?=,[^)]*[^5]*$)","0."," 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})][k<4::2],str([*zip(*g)][::-1]))),k-1)


def p(g):E=enumerate;(y,*_,Y),(x,*_,X)=map(sorted,zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]));f=sum(g,[]);c,={*f}-{0,5};return[[v|c*((x<j<X)*(i in{y+1,Y-1})|(y<i<Y)*(j in{x+1,X-1}))for j,v in E(r)]for i,r in E(g)]

### mwi (134 bytes)
p=lambda g,k=27,w=0:-k*g or[[a+[(0is a<w<20<k)*max({*sum(g,r)}-{5}),0.][6>w]for a in r]for*r,in zip(*p(g,k-1))if[w:=w*2+max(r)]][::-1]

##
import re;p=lambda g:[g:=eval(r(" 0(?=..[-5])",str(max({*g[6]}-{5})),r(" [^5](?=,[^)]*[^5]*$)","-0.",str([*zip(*g)][::-1]))))for r in[re.sub]*8][7]

# 144b, only fails 8 testcases with {*g[6]} cheese
p=lambda g,k=19,w=0:-k*g or p([[b:=a+[(b*0is not 0is a)*max({*g[6]}-{5}),0.][k>6>w]for a in r]for*r,in zip(*g)if[w:=w*2+max(r),b:=1]][::-1],k-1)

import re;p=lambda g:[g:=eval(r(" 0(?=..[-5])",max(set(g:=r(" [^5](?=,[^)]*[^5]*$)","-0.",str((*zip(*g),)[::-1])))-{"5"}),g))for r in[re.sub]*8][7]
import re;p=lambda g:[g:=eval(r(" 0(?=, 0.0|, 5)",max(set(g:=r(" [^5](?=,[^)]*[^5]*$)","0.",str([*zip(*g)][::-1])))-{*"[5]"}),g))for r in[re.sub]*8][7]
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[0, ]*5?[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]
import re;p=lambda g:[g:=eval(re.sub(*a,str([*zip(*g)][::-1])))for a in[[" 0(?=,[0, ]*5?[^5]*$)","0."]]*4+[[" 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]

### joking (165 bytes)
# feels golfable
p=lambda i,k=3,s=0,S=sum:-k*i or p([[y|(s==5in{*(h:=[*map(S,i)])[b+1:]}&{*h[:b]})*S({*S(i,[-5])})for b,y in enumerate(x)]+0*[s:=s*2+S(x)]for x in zip(*i)][::-1],k-1)

## no enumerate
p=lambda i,k=3,s=0:-k*i or p([[s:=s*2+max(x),b:=0]and[y|(5in{*(h:=[*map(max,i)])[:b]}&{*h[(b:=b+1):]}!=5<s<20)*sum({*sum(i,[])},-5)for y in x]for x in zip(*i)][::-1],k-1)

### combined (171 bytes)
p=lambda i,k=3,s=0:-k*i or p([[y or(s==5in{*(h:=[*map(max,i)])[b+1:]}&{*h[:b]})*sum({*sum(i,[])},-5)for b,y in enumerate(x)]*1**(s:=s*2+max(x))for x in zip(*i)][::-1],k-1)
