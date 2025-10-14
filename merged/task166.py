# joking (63 vs 61 bytes for gold)
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

### ovs (64 bytes)
p=lambda a:[[v or any(c*b)*2for v,c in zip(b,max(a))]for b in a]

## +1:

p=lambda g:[[v or 2*any(c)*any(r)for*c,v in zip(*g,r)]for r in g]
p=lambda g:[[v or(8in{*c}&{*r})*2for*c,v in zip(*g,r)]for r in g]
p=lambda g:[[v or(8in c!=8in r)*2for*c,v in zip(*g,r)]for r in g]
p=lambda a:[[8%(d-~any(b)+any(c))for*c,d in zip(*a,b)]for b in a]
p=lambda a:[[sum({*b}&{*c})*~d%10for*c,d in zip(*a,b)]for b in a]

### att (65 bytes)
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]

### combined (65 bytes)
p=lambda i:[[~y*max({*x}&{*t})%10for*t,y in zip(*i,x)]for x in i]
