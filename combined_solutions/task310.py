import re
p=lambda m:[*map(eval,re.findall((c:=min(s:=str(m)+'[]'*8,key=s.count))+"[^[]*"+c,s))]