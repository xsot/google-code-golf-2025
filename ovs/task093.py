import re
p=lambda g:[g:=eval(re.sub("[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])])))for _ in g][11]
