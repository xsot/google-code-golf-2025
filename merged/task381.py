# combined (94 vs 87 bytes for gold)
import re
p=lambda i:eval(re.sub("(?<=.{30}2, )([0, ]+)(?=2.{30})","*[9]*len([\\1]),",str(i)))
