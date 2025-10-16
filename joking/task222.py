p=lambda g:[g:=[[c*(str(g).count(t:=f"{c}, ")>8!=t*2in"%s"%r)for c in r]for*r,in zip(*g)]for _ in g][5]

## i wonder if there's a way to combine the str(x).count(t)>n formula
p=lambda g:[g:=[[c*(str(g).count(t:=f"{c}, "*2)>2!=t in"%s"%r)for c in r]for*r,in zip(*g)]for _ in g][5]