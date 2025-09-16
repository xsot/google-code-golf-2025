# joking (115 vs 105 bytes for gold)
p=lambda i,k=39:-k*i or[[x[-b]or 5in x[:-b]and 2-x[~b]%5&1-x[(-b<9)-b]for b in range(-9,1)]for x in zip(*p(i,k-1))]

### combined (117 bytes)
p=lambda i,k=39:-k*i or[[x[b]or 5in x[:b]and 2-x[b-1]%5&1-x[b+(b<9)]for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
