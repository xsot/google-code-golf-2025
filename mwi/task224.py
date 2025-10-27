import re;p=lambda g:[g:=eval(r(" 0(?=, 0.0|, 5)",max(set(g:=r(" [^5](?=,[^)]*[^5]*$)","0.",str([*zip(*g)][::-1])))-{*"[5]"}),g))for r in[re.sub]*8][7]

##
import re;p=lambda g:[g:=eval(re.sub(" 0(?=,"+a,b,str([*zip(*g)][::-1])))for a,b in[["[0, ]*5?[^5]*$)","0."]]*4+[[" 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]
import re;p=lambda g:[g:=eval(re.sub(*a,str([*zip(*g)][::-1])))for a in[[" 0(?=,[0, ]*5?[^5]*$)","0."]]*4+[[" 0(?=, 0.0|, 5)",max({*str(g)}-{*"[5]"})]]*4][7]