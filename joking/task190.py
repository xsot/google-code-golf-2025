import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=.{34}(.), 0.{31}\\1)","\\1",str(p(i,k-1))))[::-1])]

##
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=.{28}(.).{28}\\1, 0)","\\1",str(p(i,k-1))))[::-1])]
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=(.{28}([^0])){2}, 0)",r"\2",str(p(i,k-1))))[::-1])]
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=(.{31}0, ([^0])){2})",r"\2",str(p(i,k-1))))[::-1])]