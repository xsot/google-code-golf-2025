p=lambda g,*G:sum([[[2,*r,2]]*({*r}=={2}or({*r}-{2}!={0})*str(g).count('2')//12)for*r,in zip(*G or p(g,*g))],[])
