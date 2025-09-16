p=lambda a:[b[:4]+(a.pop()[:4]+c)[::-1]for*c,b in[*zip(*a,a)]]

##

p=lambda g:[a[:3]+[5,*b,5]+c[2::-1]for a,*b,c in zip(g,*g[::-1],g[::-1])]
