import re
p=lambda a,n=-7:n*a or eval(re.sub('0(?=([0, ]*8|(?<=[58], 0))[^)]*5)','8',str([*zip(*p(a,n+1))][::-1])))