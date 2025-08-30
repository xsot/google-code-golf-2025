# joking+mwi (115 bytes, gold)
import re;p=lambda i,*n:eval(re.sub("1, 1, 1(.{26}), 0, 1(.{26}), 1,",r"0,2,0\1*2,2,2\2*0,2,0*",str(n or p(i,*i))))

### xsot (123 bytes)
import re
p=lambda m,i=9:-i*m or p(eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1",r'0,2,0\1 2,2,2\2 0,2,0',str(m))),i-1)
