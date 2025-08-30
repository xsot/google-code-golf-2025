import re
p=lambda i,k=7:-k*i or p(eval(re.sub(r"(((0, )*0), \[\2], \2)",r"*[2+(y==0)for y in[\1]]",re.sub("((0, )+)2, ((3, )*3)",r"*[[0]*len([\3])]*len([\1]),2,\3",str([*zip(*i[::-1])])))),k-1)