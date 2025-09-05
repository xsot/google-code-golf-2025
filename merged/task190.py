# combined (112 vs 2500 bytes for gold)
import re;p=lambda i,k=19:-k*i or p(eval(re.sub("0(?=.{34}([^0]), 0.{31}\\1)","\\1",str([*zip(*i[::-1])]))),k-1)
