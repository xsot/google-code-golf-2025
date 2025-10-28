p=lambda g:[g:=[[c*(str(r*7+g).count(2*f"{c}, ")>9)for c in r]for*r,in zip(*g)]for _ in g][5]

##

def p(g):n=len(g);R=range(n);_,a,b,c,d=max(((c-a)*(d-b),a,b,c,d)for a in R for b in R for c in R for d in R if{0}!={g[a][b]}=={g[i][j]for i in range(a,c)for j in range(b,d)});return[[g[i][j]*(a<=i<c)*(b<=j<d)for j in R]for i in R]
