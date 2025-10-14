import re;p=lambda i,*I:eval(re.sub("0, 0, 0(.{55})?"*3," 1,1,1\%d"*3%(1,2,3),str(I or p(i,*i))))

## alts
import re;p=lambda i,*I,r=[1]*3:eval(re.sub("0, 0, 0(.{55})??"*3,r"*r\1*r\2*r",str(I or p(i,*i))))