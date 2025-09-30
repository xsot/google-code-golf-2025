p=lambda a:[[v or any(c*b)*2for v,c in zip(b,max(a))]for b in a]

## +1:

p=lambda g:[[v or 2*any(c)*any(r)for*c,v in zip(*g,r)]for r in g]
p=lambda g:[[v or(8in{*c}&{*r})*2for*c,v in zip(*g,r)]for r in g]
p=lambda g:[[v or(8in c!=8in r)*2for*c,v in zip(*g,r)]for r in g]
p=lambda a:[[8%(d-~any(b)+any(c))for*c,d in zip(*a,b)]for b in a]
p=lambda a:[[sum({*b}&{*c})*~d%10for*c,d in zip(*a,b)]for b in a]
