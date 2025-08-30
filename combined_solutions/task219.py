def p(i,n=0,k=0,t=2):
 f=len(r:=[x[k:]for x in i if(t:=~any(x)%3%-~t)*any(x)])
 for l in range(3,len(i)-f):
  for x in range(f*all(sum(q:=[[0**a+b*(a!=1)for a,b in zip(s[n:],t)]for s,t in zip(i[l:],r)],[~-any(9in x[:2]for x in q),~-any(i[l-1])]))*(len(i[0])-n-k)):i[l+x%f][n+x//f]=(-q[x%f][x//f]&9)%9
 return k*i or p(i,-~n%3,n>1)