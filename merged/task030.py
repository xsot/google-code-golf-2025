# combined (97 bytes, gold)
p=lambda i:[[c*x[(H:=h.index)(1)-(j:=j-1)-H(c)]for c in h]for x in i if(h:=[*map(max,*i)],j:=11)]

### ovs (tied, 97 bytes)
p=lambda i:[[c*x[(H:=h.index)(1)-(j:=j-1)-H(c)]for c in h]for x in i if(h:=[*map(max,*i)],j:=11)]

## same length as a def-function:

def p(i):*h,=map(max,*i);j=1;H=h.index;return[[c*x[(H(1)-(j:=j-1)-H(c))%10]for c in h]for x in i]
