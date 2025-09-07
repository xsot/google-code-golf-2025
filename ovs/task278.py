p=lambda i,e=enumerate:[i:=[[y or("2, 2"in"%s"%[h[a:a+3]for h in i[b-(b>0):b+2]])*3for b,y in e(x)]for a,x in e(zip(*i))][::-1]for _ in i][3]

##

def p(g):E=enumerate;L=abs;S={(i,j)for i,r in E(g)for j,v in E(r)if v};return[[v or 3*any(L(a-I)+L(A-J)==1==L(i-I)|L(j-J)for a,A in S for I,J in S)for j,v in E(r)]for i,r in E(g)]
