p=lambda i:[i:=[[x.pop()or-(s*2^s-7)%7for s in[0]+x[:0:-1]]for*x,in zip(*i)]for _ in i][3]

##

E=enumerate
p=lambda g:[[v or max(v*95%9for r in g[i+i%~i:i+2]for v in[0,*r][j:j+3])for j,v in E(l)]for i,l in E(g)]
