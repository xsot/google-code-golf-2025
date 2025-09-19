#regex sol
import re;p=lambda i,k=3:-k*i or p(eval(re.sub(f"3(.%s.)0(?=.*4)"%{len(i)*3},r"0\1 3",str([*zip(*i)][::-1]))),k-1)