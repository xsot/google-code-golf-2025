# xsot (102 vs 94 bytes for gold)
import re
p=lambda m,i=11:-i*m or[*zip(*eval(re.sub("0(?=, [^0].{25}[^0])","7",str(p(m,i-1)[::-1]))))]
