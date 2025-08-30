# joking+mwi (104 vs 101 bytes for gold)
p=lambda i:[p:=len(i)//2+1]and[[min(y,key=y.count)for y in zip(x,t,x[p:],t[p:])]for x,t in zip(i,i[p:])]
