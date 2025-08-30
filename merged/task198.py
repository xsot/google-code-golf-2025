# att (122 bytes, gold)
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)

### joking+mwi (tied, 122 bytes)
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)

### xsot (138 bytes)
import re
p=lambda m,i=19,S=re.sub:-i*m or p([*zip(*eval(S('3(?=(, 3){5}|, 4)|(?<=[^03], )3(?=, [^03])','4',S(*'03',str(m)))))][::-1],i-1)

##
import re
p=lambda m,i=19:-i*m or p([*zip(*eval(re.sub('3(?=(, 3){5}|, 4)|(?<=[^03], )3(?=, [^03])','4',str(m).replace(*'03'))))][::-1],i-1)
