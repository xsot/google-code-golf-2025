# att (94 bytes, gold)
p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]

### att (97 bytes)
p=lambda a,n=-35:n*a or p([*zip(a.pop(-~-any(a[b:=[*map(max,a)].index(8,1)-1])*b),*a)][::-1],n+1)
