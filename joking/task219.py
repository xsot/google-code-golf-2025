def p(i,n=0,k=0):
 t=2;f=len(r:=[x[k:]for x in i if(t:=~any(x)%3%-~t)*any(x)])
 for l in range(3,len(i)-f):
  for x in range(all(sum(q:=[[0**i+r*(i!=1)for i,r in zip(i[n:],r)]for i,r in zip(i[l:],r)],[sum([9in x[:2]for x in q]+i[l-1])<1]))*(len(i[0])-n-k)*f):i[l+x%f][x//f+n]=(-q[x%f][x//f]&9)%9
 return k*i or p(i,-~n%3,n>1)