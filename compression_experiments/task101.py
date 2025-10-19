def p(f):
 o,n,d,e,a=[{r+m*20for m in range(len(f))for r in range(len(f[m]))if f[m][r]==b}for b in range(5)]
 for b in d:e|={b for b in d for m in n|e if abs(b-m)in[1,20]}
 for b in d:i={b}-a and{b-min(len({b+m*(g-2)for g in range(5)}&d)for m in[1,20])*(min(e)-max(e))}&d;a|=i;f=[[f[m][r]or r+m*20in(i and{b-min(len({b+m*(g-2)for g in range(5)}&d)for m in[1,20])*(min(e)-m)for m in n})for r in range(len(f[m]))]for m in range(len(f))]
 return f