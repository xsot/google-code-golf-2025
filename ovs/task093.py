import re;p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("[^50],([^[(]+5)",r"\1,5",str(g))));'*12)or g
