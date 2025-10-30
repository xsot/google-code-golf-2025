# att (60 bytes, gold)
p=lambda a:[[d^c^b[0]or d for*_,c,d in zip(*a,b)]for b in a]

### combined (tied, 60 bytes)
p=lambda i:[[y^e^x[0]or y for y,e in zip(x,i[0])]for x in i]

### joking (64 bytes)
# recursion experiments
p=lambda a,*w:a*0!=0and[*map(p,a,a[:1]*99,*w)]or a^w[0]^w[1]or a
