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
