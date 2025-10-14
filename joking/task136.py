import re;p=lambda m,i=30:i and p(re.sub(r:="(?<=(%d.{34}){2})0"%(i%4),r[5],str(m))[::-1],i-1)or eval(m)

##
import re;p=lambda m:[m:=eval(re.sub("0(?=(.{34}1){2})|(?<=((2).{34}){2})0",r"1\3%5",str(m)))for _ in m][9]