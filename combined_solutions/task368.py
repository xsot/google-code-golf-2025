import re
def p(i):
 def t(m,q=[-1]*99):q[y:=m.end()%32]+=1;return re.findall("([^50](, [1-46-9])+)",str(i)*9)[q[y]][0]
 return eval(re.sub("5(, 5)+",t,str(i)))