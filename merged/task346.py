# joking+mwi (94 vs 58 bytes for gold)
import re;p=lambda i:[[n for n in{*sum(i,[])}-{0}if re.sub(f".*{n}, {n}, {n}.*"*2,"",str(i))]]

### xsot (111 bytes)
import re
p=lambda m:[[int(re.findall(r'([1-9], )\1\1.{%d}\1(.), \1.{%d}'%((len(m[0])*3-7,)*2),str(m))[0][1])]]

###
import re
p=lambda m:[[int(re.findall(r'([1-9], )\1\1.{%d}\1(.), \1.{%d}'%((len(m[0])*3-7,)*2),str(m))[0][1])]]

import re
p=lambda m:[[int(re.findall(r'([1-9]), \1, \1.{%d}\1, (.), \1.{%d}\1, \1'%((len(m[0])*3-5,)*2),str(m))[0][1])]]

import re
p=lambda m:[[int(re.findall(r'([^0])\1%s\1(.)\1%s\1\1'%(('.'*~-len(m[0]),)*2),str(m).replace(']',']#')[2::3])[0][1])]]

import re
p=lambda m:[[int(re.findall(rf'([^0])\1\1{(s:='.'*(len(m[0])-2))}\1(.)\1{s}\1\1\1',str(m).replace(']',']#')[2::3])[0][1])]]

import re
p=lambda m:[[int(re.findall(rf'([^0])\1\1{(s:='.'*(len(m[0])-3))}\1(.)\1{s}\1\1\1',str(sum(m,[]))[1::3])[0][1])]]

p=lambda m:[[m[r][c]for r in range(1,len(m)-1)for c in range(1,len(m[0])-1)if len(s:={m[r+i//32-2][c+i%4-1]for i in b' @`!a"Bb'})==1>0!=min(s)!=m[r][c]][:1]]

### ovs (112 bytes)
S=lambda g:zip(g[1:],g[2:],g)
p=lambda g:[[v for r in S(g)for(v,*q),a,b in zip(*map(S,r))if not{0,v}&{*q,*a+b}]]
