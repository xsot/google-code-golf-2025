import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 0.%s.5, 5)"%{len(m)*3},"3**i%5",str(p(m,i-1))))[::-1])]

##

E=enumerate
p=lambda g:[[v+sum(k*((t:=(g+g)[i-(~-k&2)+1]+[0])[s:=j-(-1)**k]>t[j]|[*g[i],0][s])for k in(1,2,3,4))for j,v in E(r)]for i,r in E(g)]
