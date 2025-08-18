import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)","1",'%len(m*3)*98+f'"{m}"'+')[::-1]'*98))
##
import re
p=lambda m:eval(eval('(m:=re.sub("0(?=..1|..{%d}1)","1",str(m))[::-1]),'%len(m*3)*98)[-1])
import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)","1",'%len(m*3)*98+f'"{m}"'+')[::-1]'*98))
import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)"%len(m*3),"1",'*98+f'"{m}"'+')[::-1]'*98))
import re
p=lambda m:eval(eval('(s:="%r")'%m+'and(s:=re.sub("0(?=..1|..{%d}1)"%len(m*3),"1",s)[::-1])'*98))