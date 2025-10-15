# alts
p=lambda a:[[d|2&~len({*b}&{*c})for*c,d in zip(*a,b)]for b in a]
##
p=lambda a:[[d^2^2*any(min(b,c))for*c,d in zip(*a,b)]for b in a]