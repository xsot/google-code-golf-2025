# ovs (187 vs 156 bytes for gold)
def p(g):e=enumerate;C=max(sum(g,[]));[g:=[[c or _*any(any(s[x+x%~x:x+2])for s in g[y+y%~y:y+2])for x,c in e(r)]for y,r in e(g)]for _ in[5,*[5]*(f"{C}, 0, 0, {C}"in str(g)),C]*3];return g

##

R=range(10)
J=1j
def p(g):
 S={i*J+j:v for i in R for j in R if(v:=g[i][j])};a={(a*-~k-b*k,d)for d in[-J,1,J,-1]for a in S for b in S if{a+d,a+d*J,b+d,b+d*J}<{*S}for k in R}
 for i,n in a:
  for d in n,n*J:
   I=i
   for*_,k in[S]*12:S[I]=S[k];I=[I+d,i][I+d in[*zip(*a)][0]]
 return[[S.get(i*J+j,5)for j in R]for i in R]

### combined (203 bytes)
def p(g):
 e=enumerate;C=max(sum(g,[]));o=2+(f"{C}, 0, 0, {C}"in str(g))
 for k,_ in e(g):g=[[c or any(any(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])*[C,5][k%o<o-1]for x,c in e(r)]for y,r in e(g)]
 return g
