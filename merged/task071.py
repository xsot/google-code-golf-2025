# combined (247 vs 122 bytes for gold)
p=lambda i,n=11,s=0,l=-1:all(len({*c,l})<3for x in i for c in zip(x[n:],x[n-s::-1]))and[[[y,*x[2*n-b-s:]][y==l]for b,y in enumerate(x)]for x in i]or p(i,n-s,1-s,max(sum(i,[]),key=lambda q:{q,0}>{c[0]for x in i for c in zip(x,*i)if q in{*x}&{*c}}))
