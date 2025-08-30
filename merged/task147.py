# joking+mwi (88 vs 84 bytes for gold)
p=lambda i,k=3:-k*i or[[y+-y%~z%8for y,z in zip(x,[0,*x])]for x in zip(*p(i,k-1))][::-1]

### ovs (tied, 88 bytes)
p=lambda g,k=-3:g*k or p([[a+-a%~b%8for a,b in zip(r,[0]+r)]for*r,in zip(*g[::-1])],k+1)
