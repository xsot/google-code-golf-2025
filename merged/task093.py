# ovs (100 vs 98 bytes for gold)
import re
p=lambda g:[g:=eval(re.sub("[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])])))for _ in g][11]

### xsot (102 bytes)
import re
p=lambda g,k=11:-k*g or[*zip(*eval(re.sub(r"[^50],([^[(]+5)",r"\1,5",str(p(g,k-1)[::-1]))))]

##
import re
p=lambda g,k=11:-k*g or p(eval(re.sub(r"[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])]))),k-1)

### combined (105 bytes)
import re
p=lambda g,k=11:-k*g or p(eval(re.sub(r"[^50],([, 0]+)5",r"\1 5,5",str([*zip(*g[::-1])]))),k-1)
