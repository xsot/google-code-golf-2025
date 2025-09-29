p=lambda g,*G:sum([[[2,*r,2]]*[str(g).count('2')//12,all(r)][{*r}<={0,2}]for*r,in zip(*G or p(g,*g))],[])
