# ovs (90 vs 86 bytes for gold)
p=lambda i:[*zip(*len(u:=[s for r in i if(s:=sum({*r}-{5}))])%len(i)*[u]or p([*zip(*i)]))]

## 87 probably looks more like this:
p=lambda i,k=11:-k*i or p([*zip(*[i,[u:=i[0][k%3::3]]*len(u)][all(u)-1in i[0]][::-1])],k-1)
p=lambda i,k=11:-k*i or p([*zip(*[i,[u:=i[0][k%3::3]]*len(u)][0in{*i[0]}-{*u}][::-1])],k-1)

### att (94 bytes)
p=lambda i:[*zip(*[u:=[*filter(int,w:=[sum({*r}-{5})for r in i])]]*len(u)*(u>w)or p(zip(*i)))]

### xsot (109 bytes)
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[*filter(int,i[0])]]or[*zip(*p([*zip(*i[::-1])]))][::-1]

### combined (111 bytes)
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[k for k in i[0]if k]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
