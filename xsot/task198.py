import re
p=lambda m,i=19,S=re.sub:-i*m or p([*zip(*eval(S('3(?=(, 3){5}|, 4)|(?<=[^03], )3(?=, [^03])','4',S(*'03',str(m)))))][::-1],i-1)

##
import re
p=lambda m,i=19:-i*m or p([*zip(*eval(re.sub('3(?=(, 3){5}|, 4)|(?<=[^03], )3(?=, [^03])','4',str(m).replace(*'03'))))][::-1],i-1)