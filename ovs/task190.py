import re;p=lambda i:exec(r"i[::-1]=zip(*eval(re.sub('.{31}0, ([^0])'*2,r'|\1\g<0>',str(i))));"*20)or i
