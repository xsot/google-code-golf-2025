import re
p=lambda i:eval(re.sub("(?<=5.{28}5, )5(?=, 5.{28}5)","2",str(i)))