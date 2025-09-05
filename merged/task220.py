# combined (113 vs 2500 bytes for gold)
p=lambda i,e=enumerate:[[y or max(max(s[b-(b>0):b+2])for s in i[a-(a>0):a+2])*5%9for b,y in e(x)]for a,x in e(i)]

### ovs (116 bytes)
E=enumerate
p=lambda g:[[v or max(v*95%9for r in g[i+i%~i:i+2]for v in[0,*r][j:j+3])for j,v in E(l)]for i,l in E(g)]
