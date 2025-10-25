# att (116 bytes, gold)
import re;p=lambda i,k=79:-k*i or p(eval(re.sub('8(?='+k//64*', 4|, 6'+'.{43}6)','k>>4',str([*zip(*i[::-1])]))),k-1)

### ovs (120 bytes)
import re;p=lambda i:[i:=eval(re.sub('[83](?='+(k>'3')*', 4|, 6'+'.{43}6)',k,str([*zip(*i[::-1])])))for k in'344'*6][15]

##
import re;p=lambda i:[i:=eval(re.sub('[83](?='+k*', 4|, 6'+'.{43}6)','k+3',str([*zip(*i[::-1])])))for k in[0,1,1]*6][15]

### joking (122 bytes)
import re;p=lambda i,k=15:-k*i or p(eval(re.sub('[83](?='+k*k%3*', 4|, 6'+'.{43}6)','k*k%3+3',str([*zip(*i[::-1])]))),k-1)

### mwi (141 bytes)
p=lambda i,k=15,r=range(15):-k*i or p([[(y:=i[~b][a])*(y&4>0)or(3<i[~b][a-1]&i[-b][a]<7)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)

### combined (156 bytes)
p=lambda i,k=11,r=range(15):-k*i or p([[(y:=i[~b][a])*(y%6%4<1)or(i[-b][a]==4or i[~b][a-1]&i[-b][a]==6)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)
