p=lambda i,*c:[*map(min,i,[9,9]+i[::-1],c)]or[i:=[*map(p,i,*i)]for _ in i][2]

##
p=lambda i,k=2:-k*i or p([[*map(min,a,[9,9]+a[::-1],c)]for*c,a in zip(*i,i)],k-1)
p=lambda i,k=2:-k*i or p([[*map(min,a,b,c)]for a,b,*c in zip(i,i[:2]+i[::-1],*i)],k-1)