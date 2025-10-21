# recursion experiment
p=lambda a,s=[],*r:a*0!=0and[*map(p,a,[a]*9,*s)]*2or a or any(r)*8