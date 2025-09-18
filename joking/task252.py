p=lambda a:[(i:=1)*[(i:=-i)*4%(c+4)for c in b]for b in a]

## alts
p=lambda a:[(i:=4)and[(i:=-i)%(c+4)for c in b]for b in a]
p=lambda a:[[(i:=-i)%(c+4)for c in b]for b in a if[i:=4]]

#and regex, for fun
import re;p=lambda i:eval(re.sub("(\d, .)",r"\1and 4",str(i)))