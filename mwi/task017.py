R=range(21);p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)

## Approach copied from task110, fails 1 testcase
p=lambda g,k=-3:k*g or p([*zip(*[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g])],k+1)