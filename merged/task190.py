# joking (108 vs 105 bytes for gold)
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=.{34}(.), 0.{31}\\1)","\\1",str(p(i,k-1))))[::-1])]

##
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=.{28}(.).{28}\\1, 0)","\\1",str(p(i,k-1))))[::-1])]
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=(.{28}([^0])){2}, 0)",r"\2",str(p(i,k-1))))[::-1])]
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=(.{31}0, ([^0])){2})",r"\2",str(p(i,k-1))))[::-1])]

### combined (112 bytes)
import re;p=lambda i,k=19:-k*i or p(eval(re.sub("0(?=.{34}([^0]), 0.{31}\\1)","\\1",str([*zip(*i[::-1])]))),k-1)
