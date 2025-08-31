# att (87 vs 81 bytes for gold)
p=lambda a:[b.count(e)*[e]for b in a if(e:=min(set(d:=sum(a,[]))-{0},key=d.count))in b]

### combined (tied, 87 bytes)
p=lambda a:[b.count(e)*[e]for b in a if(e:=min(set(d:=sum(a,[]))-{0},key=d.count))in b]

### xsot (106 bytes)
import re
p=lambda m:[*map(eval,re.findall(f"(?:{min(set(a:=sum(m,[]))-{0},key=a.count)}[, ]*)+",str(m)))]
