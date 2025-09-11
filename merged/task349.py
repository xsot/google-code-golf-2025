# combined (237 (261 unzipped) vs 214 bytes for gold)
p=lambda i,n=6,l=0,R=range:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3or 9in[*zip(*i[:x+1])][y]for y in R(l)]for x in R(l)]for a in R(-n*2,l)for b in R(l-n*2+1)if{min(x[max(b,0):b+n*2])for x in i[max(a,0):a+n*2]}=={9}]]and p(i,n-1,len(i))
