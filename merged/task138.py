# joking+mwi (152 vs 107 bytes for gold)
p=lambda i,k=3,e=enumerate:-k*i or[[y or(x[0]in x[b:])*x[0]for b,y in e(x)]for x in zip(*p([*zip(*i[:min(n-1for n,s in e(i)if min(s)):-1])],k-1))][::-1]
