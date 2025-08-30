import re
p=lambda i:eval(re.sub(r"(([^0])(, .)+), 0(?=.*\2.*\].*\2)",r"0,\1",str(i)))