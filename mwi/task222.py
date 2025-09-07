# 15 seconds, 104b
p=lambda g:[g:=[[c*(2*f"{c}, "in str(r))*(sum(g,g).count(c)>4)for c in r]for r in zip(*g)]for _ in g][5]
## 5 seconds, 105b
p=lambda g,k=5:-k*g or p([[c*(2*f"{c}, "in str(r))*(sum(g,g).count(c)>4)for c in r]for r in zip(*g)],k-1)