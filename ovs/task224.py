import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[^)]*[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]

##
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(" 0(?=,"+["[^)]*[^5]*$)"," 0.0|, 5)"][k<4],["0.",max({*str(g)}-{*"[5]"})][k<4],str([*zip(*g)][::-1]))),k-1)
import re;p=lambda g,k=7:-k*g or p(eval(re.sub(*[" 0(?=,[^)]*[^5]*$)","0."," 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})][k<4::2],str([*zip(*g)][::-1]))),k-1)


def p(g):E=enumerate;(y,*_,Y),(x,*_,X)=map(sorted,zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]));f=sum(g,[]);c,={*f}-{0,5};return[[v|c*((x<j<X)*(i in{y+1,Y-1})|(y<i<Y)*(j in{x+1,X-1}))for j,v in E(r)]for i,r in E(g)]
