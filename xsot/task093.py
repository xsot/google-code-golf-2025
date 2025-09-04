import re
p=lambda g,k=11:-k*g or[*zip(*eval(re.sub(r"[^50],([^[(]+5)",r"\1,5",str(p(g,k-1)[::-1]))))]

##
import re
p=lambda g,k=11:-k*g or p(eval(re.sub(r"[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])]))),k-1)
