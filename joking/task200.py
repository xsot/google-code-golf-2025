p=lambda g,P=[0]*9:[*zip(*([P*2]*g[9].index(c:=max(g[9]))+[C:=[c]*10,[5]+P,C,P+[5]]*9)[:10])]

##
p=lambda g:[[c:=0,n:=0]and[(c:=c|b)and[a//9*5,c,5*0**a,c][n:=-~n%4]for b in g[9]]for a in range(10)]