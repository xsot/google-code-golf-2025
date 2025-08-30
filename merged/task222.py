# ovs (230 vs 144 bytes for gold)
def p(g):n=len(g);R=range(n);_,a,b,c,d=max(((c-a)*(d-b),a,b,c,d)for a in R for b in R for c in R for d in R if{0}!={g[a][b]}=={g[i][j]for i in range(a,c)for j in range(b,d)});return[[g[i][j]*(a<=i<c)*(b<=j<d)for j in R]for i in R]
