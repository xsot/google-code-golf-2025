import re;p=lambda i:exec('i[::-1]=zip(*eval(re.sub("0(?=.{34}[38].{34}[382])","3",str(i))));'*40)or i

##
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)
