# combined (105 vs 2500 bytes for gold)
p=lambda i,k=3:-k*i or[[x[b]or(sum(x[:b])%8|1in x[:4])*8for b in range(10)]for x in zip(*p(i,k-1)[::-1])]

### att (115 bytes)
import re
p=lambda a,n=-7:n*a or eval(re.sub('0(?=([0, ]*8|(?<=[58], 0))[^)]*5)','8',str([*zip(*p(a,n+1))][::-1])))
