import re;p=lambda i:eval(re.sub(r"(.),(?=.*\1.*0, \1)",r"0,\1|",str(i)))

##
p=lambda g,s=0:g and[[[v,j][{*g[0]}<={*sum(g[min(2,s:=s+(v>0)):],[])}]for j,v in zip([0]+g[0],g[0])]]+p(g[1:])
