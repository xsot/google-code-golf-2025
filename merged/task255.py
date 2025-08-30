# ovs (381 vs 280 bytes for gold)
def p(g):
 for R in[lambda x:[r[::-1]for*r,in zip(*x)]]*4:
  c,={*sum(g:=R(g),[])}-{0,3};D=*[[*r,c].index(c)for r in g],99,0;j=-1
  while(i:=j+1)<30:
   while 10<D[j:=j+1]:0
   for r in g[i+(i>0):j+j%~j]:w=min(D[i:j])-1;r[:w]=[3]*w
 for _ in g*2:
  for r in(m:=(g:=R(g))[:[*[3in(a,b)for a,*_,b in g],1].index(1)]):r[:]=[v*(v!=3or[*f,f[0]].count(3)>2)for*f,v in zip(*m,r)]
 return g
