import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m:re.findall("[^50](?:, [1-9])+",s*2)[-s[m.end()-1::32].count('5')],s:=str(i)))