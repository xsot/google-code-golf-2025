# joking+mwi (105 vs 102 bytes for gold)
import re
p=lambda g,k=11:-k*g or p(eval(re.sub(r"[^50],([, 0]+)5",r"\1 5,5",str([*zip(*g[::-1])]))),k-1)
