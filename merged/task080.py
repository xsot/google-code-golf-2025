# combined (253 (272 unzipped) bytes, gold)
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]

### ovs (453 bytes)
def p(g):
 e=enumerate;t=6,11,10,7;E=[A+1for A,B in e(g)if len({*B})==1][0];c=[A[::E]for A in g[::E]];J=lambda A,B:len(c)>A>-1<B<len(c)
 for A,B in e(c):
  for C,y in e(B):
   if sum(J(o:=A+P%3-1,z:=C+P%5-1)>0<y*c[o][z]for P in t)>3:
    for K,B in e(c):
     for L,R in e(B):
      for P in t+(0,12,5,2):
       H=P%3-1;I=P%5-1
       if(R==y)*J(A+H,C+I)*J(K+H,L+I):c[K+H][L+I]=c[A+H][C+I]
    return[[y or c[A//E][C//E]for C,y in e(B)]for A,B in e(g)]
