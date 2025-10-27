import re;p=lambda i:exec(r'i[::-1]=zip(*eval(re.sub(r"0(?=(.{35})+,( [^0]).{27}\2,\2)",r"\2",str(i))));'*4)or i
