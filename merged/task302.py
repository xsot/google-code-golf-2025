# ovs (91 bytes, gold)
import re;p=lambda i:eval(re.sub("5,([ 0,]*)5(?!, 5)",r"5,*[5+(r:=len([\1]))]*r,5",str(i)))

### combined (93 bytes)
import re
p=lambda i:eval(re.sub("5,([ 0,]*)5(?=, 0|])",r"5,*[5+(r:=len([\1]))]*r,5",str(i)))
