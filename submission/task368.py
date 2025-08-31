import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m,q=[re.findall("([^50](, [1-9])+)",str(i)*9)for _ in i]:q[m.end()%8].pop(0)[0],str(i)))