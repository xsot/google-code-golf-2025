# joking (106 bytes, gold)
import re;p=lambda i,k=39:-k*i or[*zip(*eval(re.sub("0(?=.{34}[38].{34}[382])","3",str(p(i,k-1))))[::-1])]

### ovs (127 bytes)
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)

### combined (127 bytes)
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)
