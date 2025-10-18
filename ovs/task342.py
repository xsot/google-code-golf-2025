import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub("([1-9])((.{32})+?[0, ]+)8",r"0\2\1",str(p(i,k-1)))))][::-1]
