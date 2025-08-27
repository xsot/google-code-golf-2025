import re
p=lambda m:[*map(eval,re.findall(f"(?:{min(set(a:=sum(m,[]))-{0},key=a.count)}[, ]*)+",str(m)))]