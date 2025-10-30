# att (64 bytes, gold)
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]

### ovs (tied, 64 bytes)
p=lambda g:[[v+2-2*any(r)*any(c)for*c,v in zip(*g,r)]for r in g]

### xsot (tied, 64 bytes)
# alts
p=lambda a:[[d|2&~len({*b}&{*c})for*c,d in zip(*a,b)]for b in a]
##
p=lambda a:[[d^2^2*any(min(b,c))for*c,d in zip(*a,b)]for b in a]

### combined (tied, 64 bytes)
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]

### joking (68 bytes)
# recursion experiments
p=lambda a,s=[],*w:a+2-2*any(w)*any(s)if w else[*map(p,a,[a]*99,*s)]
