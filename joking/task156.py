p=lambda i,a=9,S=sum:[[v-(S(g:=S(i,[]))//S(g[:i.index(min(i),1)*10]*2)+2^a//60)*(S(g[a-18:(a:=a+1):9])>11)for v in r]for r in i]

##
p=lambda i,a=9,S=sum:[[v-S(S(i,[])[a-18:(a:=a+1):9])//12*(S(t:=[*map(S,i)])//S(t[:t.index(0,1)]*2)+2^a//60)for v in r]for r in i]