p=lambda i,k=7:-k*i or[[*map(max,x,[0]*10+x)]for*x,in zip(*p(i,k-1))][::-1]
