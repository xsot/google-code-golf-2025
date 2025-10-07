# recursion experiments
p=lambda a,s=[],*w:a+2-2*any(w)*any(s)if w else[*map(p,a,[a]*99,*s)]