import re
p=lambda i:[i:=eval(re.sub("5((.{35})+(?=.{66}2)|[0, ]+(?=, 2))",r"0\1+5",str([*zip(*i[::-1])])))for _ in i][7]