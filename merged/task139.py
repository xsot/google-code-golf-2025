# combined (100 vs 2500 bytes for gold)
p=lambda i,k=11,r=range(9):-k*i or p([[i[~b][a]or i[-b][a]*i[~b][a-1]%3*7for b in r]for a in r],k-1)

### xsot (102 bytes)
import re
p=lambda m,i=11:-i*m or[*zip(*eval(re.sub("0(?=, [^0].{25}[^0])","7",str(p(m,i-1)[::-1]))))]
