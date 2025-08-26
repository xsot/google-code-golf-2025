import re
p=lambda m,i=291:-i*m or p([*zip(*eval(re.sub("0(?=, ([^08]))",lambda x:s.strip(", 08[]()"+x[1])[0],s:=str(m))))][::-1],i-1)