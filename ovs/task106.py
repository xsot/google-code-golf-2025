S='[::-1]for*x,a in zip(*i,i)]';p=eval(f'lambda i:[a+x{S}+[x+a'+S+S[:6])

##

p=lambda g,i=0:g[i:]and[w:=g[i]+[*[*zip(*g)][i]][::-1],*p(g,i+1),w[::-1]]
