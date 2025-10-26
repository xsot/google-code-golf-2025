p=lambda i:[*zip(*len(u:=[s for r in i if(s:=sum({*r}-{5}))])%len(i)*[u]or p([*zip(*i)]))]

## 87 probably looks more like this:
p=lambda i,k=11:-k*i or p([*zip(*[i,[u:=i[0][k%3::3]]*len(u)][all(u)-1in i[0]][::-1])],k-1)
p=lambda i,k=11:-k*i or p([*zip(*[i,[u:=i[0][k%3::3]]*len(u)][0in{*i[0]}-{*u}][::-1])],k-1)
