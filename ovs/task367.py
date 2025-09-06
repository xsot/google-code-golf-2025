import re
p=lambda g,k=-23:k*g or p(eval(re.sub(f"(0.{(N:={len(g)*3-2})}0, 5, 5.{N}5,|4,) 0","\\1 4",str([*zip(*g)][::-1]))),k+1)
