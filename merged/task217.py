p=lambda a,*n:[*filter(any,zip(*[[d&e for d in b for e in c]for b in n for c in a]or p(a,*a)))]

### ovs (104 bytes)
def p(g):exec("g[:]=zip(*filter(any,g));"*2);return[[v*(w>0)for w in l for v in k]for l in g for k in g]
