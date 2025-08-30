# nomerge
import re
p=lambda m,i=11:-i*m or[*zip(*eval(re.sub("0, [02](?=.{52}[02], [02])","2,2",str(p(m,i-1)[::-1]))))]