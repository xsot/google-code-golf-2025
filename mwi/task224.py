p=lambda g,k=27,w=0:-k*g or[[a+[(0is a<w<20<k)*max({*sum(g,r)}-{5}),0.][6>w]for a in r]for*r,in zip(*p(g,k-1))if[w:=w*2+max(r)]][::-1]

##
import re;p=lambda g:[g:=eval(r(" 0(?=..[-5])",str(max({*g[6]}-{5})),r(" [^5](?=,[^)]*[^5]*$)","-0.",str([*zip(*g)][::-1]))))for r in[re.sub]*8][7]

# 144b, only fails 8 testcases with {*g[6]} cheese
p=lambda g,k=19,w=0:-k*g or p([[b:=a+[(b*0is not 0is a)*max({*g[6]}-{5}),0.][k>6>w]for a in r]for*r,in zip(*g)if[w:=w*2+max(r),b:=1]][::-1],k-1)

import re;p=lambda g:[g:=eval(r(" 0(?=..[-5])",max(set(g:=r(" [^5](?=,[^)]*[^5]*$)","-0.",str((*zip(*g),)[::-1])))-{"5"}),g))for r in[re.sub]*8][7]
import re;p=lambda g:[g:=eval(r(" 0(?=, 0.0|, 5)",max(set(g:=r(" [^5](?=,[^)]*[^5]*$)","0.",str([*zip(*g)][::-1])))-{*"[5]"}),g))for r in[re.sub]*8][7]
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[0, ]*5?[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]
import re;p=lambda g:[g:=eval(re.sub(*a,str([*zip(*g)][::-1])))for a in[[" 0(?=,[0, ]*5?[^5]*$)","0."]]*4+[[" 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]