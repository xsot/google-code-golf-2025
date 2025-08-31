# combined (101 vs 100 bytes for gold)
p=lambda i,k=0,s=[0]*99:[s+0*(s:=[*x])for x in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
