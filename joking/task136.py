import re
p=lambda m:[m:=eval(re.sub("0(?=(.{34}1){2})|(?<=((2).{34}){2})0",r"1\3%5",str(m)))for _ in m][9]