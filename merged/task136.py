# combined (113 vs 105 bytes for gold)
p=lambda i,k=19,r=range(10):-k*i or p([[i[~b][~a]or(a*b>0)*i[-b][-a]&2-k%2&i[1-b][1-a]for b in r]for a in r],k-1)

### xsot (tied, 113 bytes)
import re
p=lambda m,S=re.sub:eval(eval('S("(?<=(2.{34}){2})0","2",S("0(?=(.{34}1){2})","1",'*9+f'"{m}"'+'))'*9))

##
import re
p=lambda m,i=9,S=re.sub:-i*m or p(eval(S("(?<=(2.{34}){2})0","2",S("0(?=(.{34}1){2})","1",str(m)))),i-1)

import re
p=lambda m,i=9:-i*m or p(eval(re.sub("(?<=(2.{34}){2})0","2",re.sub("0(?=(.{34}1){2})","1",str(m)))),i-1)

import re
p=lambda m,i=20:-i*m or p(eval(re.sub("(0?(<?==((2..{{3344}}1)){{22}}))0"[i%2::2],"21"[i%2],str(m))),i-1)

import re
p=lambda m,i=20:-i*m or p(eval(re.sub(["(?<=(2.{34}){2})0","0(?=(.{34}1){2})"][i%2],"21"[i%2],str(m))),i-1)
