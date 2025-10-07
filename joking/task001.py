exec("p=lambda a:[[d&e "+"for %s in %s%s"*4%(*'db ec]ba ca]',))

## recursive
p=lambda a,c=0:a*0!=0and[p(s,t)for s in a for t in c or a]or a&c
p=lambda a,*c:[s&t if c else p(s,*t)for s in a for t in c or a]
p=lambda*a:[s*0!=0and p(s,t)or s&t for s in a[0]for t in a[-1]]
p=lambda*a:[s&t if a[1:]else p(s,t)for s in a[0]for t in a[-1]]

## doesn't work, splits up each list
p=lambda a,s=[]:s*0!=0and[*map(p,s or a,[a]*9)]or a&s