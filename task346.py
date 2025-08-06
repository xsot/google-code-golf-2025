p=lambda m:[[m[r][c]for r in range(1,len(m)-1)for c in range(1,len(m[0])-1)if len(s:={m[r+i//32-2][c+i%4-1]for i in b' @`!a"Bb'})==1>0!=min(s)!=m[r][c]][:1]]

###
import re
p=lambda m:[[int(re.findall(rf'([^0])\1\1{(s:='.'*(len(m[0])-2))}\1(.)\1{s}\1\1\1',str(m).replace(']',']#')[2::3])[0][1])]]

import re
p=lambda m:[[int(re.findall(rf'([^0])\1\1{(s:='.'*(len(m[0])-3))}\1(.)\1{s}\1\1\1',str(sum(m,[]))[1::3])[0][1])]]