import re
p=lambda m,i=31:-i*m or p(eval(re.sub(f'({7>>i%3})([^(]*)0(?=, {i%3%2+1})',r'0\2\1',str([*zip(*m)][::-1]))),i-1)

### xsot (125 bytes)
import re
p=lambda m,i=31:-i*m or p([*zip(*eval(re.sub(f'({7>>i%3})([^[(]*) 0, ({i%3%2+1})',r'0\2\1,\3',str(m))))][::-1],i-1)

##
import re
p=lambda m,i=31:-i*m or p([*zip(*eval(re.sub(f'({[7,3][c:=i%3%2]})([^[(]*), 0, ({c+1})',r'0\2,\1,\3',str(m))))][::-1],i-1)

import re
p=lambda m,i=7,S=re.sub:-i*m or p([*zip(*eval(S('7([^[(]*), 0, 1','0\\1, 7, 1',S('3([^[(]*), 0, 2','0\\1, 3, 2',str(m)))))][::-1],i-1)
