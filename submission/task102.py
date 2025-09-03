import re
p=lambda i,k=20:-k*i or p(eval(re.sub(f'({(h:=(5,)*-~(n:=k%5))}.{(s:={34-n*3})}(?={(r:=f"5, [^5]{ {n*3}}5.{s}")*n}{h})({r})*5)(, 0)+',"\\1"+",2"*n,str(i))),k-1)