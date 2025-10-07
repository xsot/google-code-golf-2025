# recursion experiments
p=lambda a,*w:a*0!=0and[*map(p,a,a[:1]*99,*w)]or a^w[0]^w[1]or a