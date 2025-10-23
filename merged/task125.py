# joking (122 vs 119 bytes for gold)
import re;p=lambda i,k=15:-k*i or p(eval(re.sub('[83](?='+k*k%3*', 4|, 6'+'.{43}6)','k*k%3+3',str([*zip(*i[::-1])]))),k-1)

### ovs (125 bytes)
import re
p=lambda i,k=15:-k*i or p(eval(re.sub('[83](?='+(k%3>0)*', 4|, 6'+'.{43}6)','344'[k%3],str([*zip(*i[::-1])]))),k-1)

### mwi (141 bytes)
p=lambda i,k=15,r=range(15):-k*i or p([[(y:=i[~b][a])*(y&4>0)or(3<i[~b][a-1]&i[-b][a]<7)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)

### combined (156 bytes)
p=lambda i,k=11,r=range(15):-k*i or p([[(y:=i[~b][a])*(y%6%4<1)or(i[-b][a]==4or i[~b][a-1]&i[-b][a]==6)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)
