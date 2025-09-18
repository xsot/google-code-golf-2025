# att (68 bytes, gold)
p=lambda a:[p(b)for*b,in map(zip,a,a[5:])]or max(sum(a,()),key=bool)

### joking (74 bytes)
p=lambda i:[p([*zip(i.pop(0),n)])for n in i[5:]]or max(sum(i,()),key=bool)

##
p=lambda i:(t:=[*i])[4:]and[*map(p,map(zip,t,t[5:]))]or max(sum(t,()),key=bool)
p=lambda*i:i[0]*0!=0and[*map(p,*sum([[a,a[5:]]for a in i],[]))]or max(i,key=bool)
p=lambda*i:i[0]*0!=0and[*map(p,*[a[x:]for a in i for x in[0,5]])]or max(i,key=bool)
p=lambda i,*w:i*0!=0and[*map(p,i,i[5:],*w and[*w,w[0][5:]])]or max([i,*w],key=bool)

### combined (75 bytes)
p=eval('lambda a:[[max(sum(a,()),key=bool)'+'for*a,in map(zip,a,a[5:])]'*2)

### ovs (88 bytes)
p=lambda g:[[[*filter(abs,u),0][0]for u in zip(a,a[5:],b,b[5:])]for a,b in zip(g,g[5:])]
