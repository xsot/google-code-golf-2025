import re
p=lambda i,k=12,r=range(4):-k*[[0]*4]or[[(a+b<2)*int(re.search(r"([1-9]), \1.{37}\1",str(i))[1])or p([*zip(*i[::-1])],k-4)[b][~a]for b in r]for a in r]