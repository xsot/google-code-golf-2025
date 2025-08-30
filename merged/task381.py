# joking+mwi (100 vs 87 bytes for gold)
import re
p=lambda i:i[:1]+eval(re.sub("2, ((0, )+)(?=2)","2,*[9]*len([\\1]),",str(i[1:-1])))+i[-1:]
