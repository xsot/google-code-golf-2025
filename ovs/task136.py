import re;p=lambda m:eval([m:=re.sub("(?<=(%s.{34}){2})0"%i,i,str(m))[::-1]for i in'2103'*9][29])
