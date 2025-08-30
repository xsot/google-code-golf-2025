import re
p=lambda i,k=7:-k*i or p(eval(re.sub(r"5(((.{34}0)+)(.{32})|([0, ]+)), 2",r"0\2\5+5\4,2",str([*zip(*i[::-1])]))),k-1)