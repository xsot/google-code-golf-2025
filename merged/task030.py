# ovs (97 bytes, gold)
p=lambda i:[[c*x[(H:=h.index)(1)-(j:=j-1)-H(c)]for c in h]for x in i if(h:=[*map(max,*i)],j:=11)]

## same length as a def-function:

def p(i):*h,=map(max,*i);j=1;H=h.index;return[[c*x[(H(1)-(j:=j-1)-H(c))%10]for c in h]for x in i]

### combined (127 bytes)
import re;p=lambda i:[eval(re.sub(r"((\d)(, \2)*)",r"*map(int.__mul__,x[h.index(1):],[\1])",str(h:=[*map(max,*i)])))for x in i]
