# compression_experiments (203 (277 unzipped) vs 172 bytes for gold)
p=lambda r:[r:=[[max(r[i][m],(i-n+a in range(a*4))*(m-e+a in range(a*4))*3,9in(i[m]for i in r[:i]))for m in range(len(r))]for i in range(len(r))]for a in range(len(r))for n in range(-a*2,len(r))for e in range(len(r)-a*2+1)if{min(i[e:a*2+e])for i in r[max(n,0):a*2+n]}=={9}][-1]

### joking (205 (277 unzipped) bytes)
#206
p=lambda	i:[i:=[[max(i[x][y],(x-a+n	in	range(n*4))*(y-b+n	in	range(n*4))*3,9in(x[y]for	x	in	i[:x]))for	y	in	range(len(i))]for	x	in	range(len(i))]for	n	in	range(len(i))for	a	in	range(-n*2,len(i))for	b	in	range(len(i)-n*2+1)if{min(x[b:n*2+b])for	x	in	i[max(a,0):n*2+a]}=={9}][-1]

##
p=lambda i:[i:=[[max(i[x][y],(x-a+n in range(n*4))*(y-b+n in range(n*4))*3,9in(#['x[y]for x in i[:x]','i[x][y]for x in range(x)']##))for y in range(len(i))]for x in range(len(i))]for n in range(len(i))for a in range(-n*2,len(i))for b in range(len(i)-n*2+1)if{min(x[b:n*2+b])for x in i[max(#['a,0','0,a']##):n*2+a]}=={9}]#['[-1]','*0+i']##

## 238 for unzipped
p=lambda i,r=range:(l:=len(i))*0*[i:=[[max(i[x][y],(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3,9in(x[y]for x in i[:x]))for y in r(l)]for x in r(l)]for n in r(6)for a in r(-n*2,l)for b in r(l-n*2+1)if{min(x[b:n*2+b])for x in i[max(a,0):n*2+a]}=={9}]+i

### ovs (212 (260 unzipped) bytes)
p=lambda i:[i:=[[max(i[x][y],(a<=x+n<n*4+a)*(b<=y+n<n*4+b)*3,9in(x[y]for x in i[:x+1]))for y in range(len(i))]for x in range(len(i))]for n in range(6)for a in range(-n*2,len(i))for b in range(len(i)-n*2+1)if{min(x[b:n*2+b])for x in i[max(a,0):n*2+a]}=={9}][-1]

### mwi (231 (267 unzipped) bytes)
p=lambda i,n=6,l=0:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<n*4+a)*(b<=y+n<n*4+b)*3or 9in[*zip(*i[:x+1])][y]for y in range(l)]for x in range(l)]for a in range(-n*2,l)for b in range(l-n*2+1)if{min(x[b*(b>0):n*2+b])for x in i[a*(a>0):n*2+a]}=={9}]]and p(i,n-1,len(i))

### combined (235 (261 unzipped) bytes)
p=lambda i,n=6,l=0,R=range:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3or 9in[*zip(*i[:x+1])][y]for y in R(l)]for x in R(l)]for a in R(-n*2,l)for b in R(l-n*2+1)if{min(x[max(b,0):b+n*2])for x in i[max(a,0):a+n*2]}=={9}]]and p(i,n-1,len(i))
