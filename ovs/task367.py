import re
p=lambda g,k=-23:k*g or p(eval(re.sub(f"0, (?=4|5.{(N:={len(g)*3-2})}5, 5, 0.{N}0)","4,",str([*zip(*g)][::-1]))),k+1)
