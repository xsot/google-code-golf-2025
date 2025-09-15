# mwi (233 (267 unzipped) vs 214 bytes for gold)
p=lambda i,n=6,l=0:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<n*4+a)*(b<=y+n<n*4+b)*3or 9in[*zip(*i[:x+1])][y]for y in range(l)]for x in range(l)]for a in range(-n*2,l)for b in range(l-n*2+1)if{min(x[b*(b>0):n*2+b])for x in i[a*(a>0):n*2+a]}=={9}]]and p(i,n-1,len(i))

### combined (236 (261 unzipped) bytes)
p=lambda i,n=6,l=0,R=range:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3or 9in[*zip(*i[:x+1])][y]for y in R(l)]for x in R(l)]for a in R(-n*2,l)for b in R(l-n*2+1)if{min(x[max(b,0):b+n*2])for x in i[max(a,0):a+n*2]}=={9}]]and p(i,n-1,len(i))
