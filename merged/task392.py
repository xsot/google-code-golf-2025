# ovs (320 vs 161 bytes for gold)
R=range(10)
J=1j
def p(g):
 S={i*J+j:v for i in R for j in R if(v:=g[i][j])};a={(a*-~k-b*k,d)for d in[-J,1,J,-1]for a in S for b in S if{a+d,a+d*J,b+d,b+d*J}<{*S}for k in R}
 for i,n in a:
  for d in n,n*J:
   I=i
   for*_,k in[S]*12:S[I]=S[k];I=[I+d,i][I+d in[*zip(*a)][0]]
 return[[S.get(i*J+j,5)for j in R]for i in R]
