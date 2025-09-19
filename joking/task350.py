#regex solution
import re;p=lambda i,*n:eval(re.sub("1,([^)]+?)(?=1)","1,*[8]*len([\\1]),",str([*zip(*n or p(i,*i))])))