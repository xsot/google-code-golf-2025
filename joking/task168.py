import re
p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(r"0, (?=(.{35})+([^0], ).{26}\2\2)",r"\2",str(p(i,k-1))))[::-1])]