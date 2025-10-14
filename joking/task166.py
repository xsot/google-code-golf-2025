# previous pysearch probably had any(row)&any(column)<1 and cell==8 cases included
p=lambda a:[[~v*c*any(b)%10for v,c in zip(b,max(a))]for b in a]

##
p=lambda a:[[c*max(b)>>~v%6for v,c in zip(b,max(a))]for b in a]
p=lambda g:[[max(c)*max(r)>>~v%6for*c,v in zip(*g,r)]for r in g]

## recursive experiments
p=lambda a,s=[],*r:a+~a*any(any(s)*r)%3if r else[*map(p,a,[a]*20,*s)]
p=lambda a,s=[],r=0:a*0!=0and[*map(p,a,[max(a)]*20,s+a)]or a+~a*s*r%3
p=lambda a,s=[],*r:a or 2*any(s)*any(r)if r else[*map(p,a,[a]*20,*s)]
p=lambda a,s=[],r=0:a*0!=0and[*map(p,a,[max(a)]*20,s+a)]or s*r>>~a%6
