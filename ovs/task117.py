p=lambda i:[i:=[*zip(*map(max,i,(i*2)[j*2::-1]+i[::-1]))]for j in b'	'*2if[x.count(max(i[j]))for x in i[j-2:j+3]]==[0,2,1,2,0]][1]

##

p=lambda i:[i:=[*zip(*map(max,i,(i*2)[w.index(1)*2::-1]+i[::-1]))]for n in range(20)if[*filter(abs,w:=[x.count(n%10)for x in i])]==[2,1,2]][1]
