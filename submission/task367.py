import re
p=lambda g,k=-19:k*g or p(eval(re.sub(f"0(?=, 4|.{ {N:=len(g)*3+4}}5, 0.{ {N-6}}0)","4",str([*zip(*g)][::-1]))),k+1)