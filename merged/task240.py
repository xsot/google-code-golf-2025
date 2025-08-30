# joking+mwi (107 bytes, gold)
p=lambda i,k=4,r=range(19):-k*i or p([[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r],k-1)
