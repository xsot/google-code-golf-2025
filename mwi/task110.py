# If you find a golf for this hole, try applying it to task017
p=lambda g,k=-1:k*g or p([*zip(*[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g])],k+1)

## Only fails one testcase
p=lambda g:[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g]