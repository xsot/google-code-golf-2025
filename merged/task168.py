# combined (117 vs 2500 bytes for gold)
import re
p=lambda i,k=39:-k*i or[*zip(*eval(re.sub(r"0((.{35})+, ([^0]).{28}\3, \3)",r"\3\1",str(p(i,k-1))))[::-1])]
