import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub(f"0(?=, 0.{ {len(m)*3}}.5, 5)","3**i%5",str(p(m,i-1))))[::-1])]