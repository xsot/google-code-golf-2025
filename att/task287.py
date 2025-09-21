p=lambda*a:a[2:]and max({*a}-{4})or[*map(p,*a,a[0][::-1])]

##
p=lambda*a:a[2:]and sum({*a,4})-4or[*map(p,*a,a[0][::-1])]
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]