p=lambda a,n=10,d=0:~n*a or p([[b.pop()|(n%6*2in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-3)

## almost identical to 246
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k*6+2in x)*4for y in x],*i)],k-1)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|(n%6*2in b)*(d:=~9%~sum(c)+d&4)for c in a[::-1]]for*b,in zip(*a)],n-3)
p=lambda a,n=15,d=0:-n*a or p([[b.pop()|(n*7&26in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-2)
p=lambda a,n=23,d=0:-n*a or p([[b.pop()|(-~n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)
p=lambda a,n=24,d=0:n and p([[b.pop()|(n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)or a
p=lambda a,n=25,d=0:1//n*a or p([[b.pop()|(n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|4*(n%6*2in(d:=d^-5%~sum(c)%3)*b)for c in a[::-1]]for*b,in zip(*a)],n-3)