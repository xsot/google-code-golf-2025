import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.*],)","*[9]*len([\\1]),",str(m)))
