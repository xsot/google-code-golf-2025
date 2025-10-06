#206
p=lambda	i:[i:=[[max(i[x][y],(x-a+n	in	range(n*4))*(y-b+n	in	range(n*4))*3,9in(x[y]for	x	in	i[:x]))for	y	in	range(len(i))]for	x	in	range(len(i))]for	n	in	range(len(i))for	a	in	range(-n*2,len(i))for	b	in	range(len(i)-n*2+1)if{min(x[b:n*2+b])for	x	in	i[max(a,0):n*2+a]}=={9}][-1]

##
p=lambda i:[i:=[[max(i[x][y],(x-a+n in range(n*4))*(y-b+n in range(n*4))*3,9in(#['x[y]for x in i[:x]','i[x][y]for x in range(x)']##))for y in range(len(i))]for x in range(len(i))]for n in range(len(i))for a in range(-n*2,len(i))for b in range(len(i)-n*2+1)if{min(x[b:n*2+b])for x in i[max(#['a,0','0,a']##):n*2+a]}=={9}]#['[-1]','*0+i']##

## 238 for unzipped
p=lambda i,r=range:(l:=len(i))*0*[i:=[[max(i[x][y],(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3,9in(x[y]for x in i[:x]))for y in r(l)]for x in r(l)]for n in r(6)for a in r(-n*2,l)for b in r(l-n*2+1)if{min(x[b:n*2+b])for x in i[max(a,0):n*2+a]}=={9}]+i