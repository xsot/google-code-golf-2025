# att (60 vs 59 bytes for gold)
p=lambda a:[[d^c^b[0]or d for*_,c,d in zip(*a,b)]for b in a]

### combined (tied, 60 bytes)
p=lambda i:[[y^e^x[0]or y for y,e in zip(x,i[0])]for x in i]
